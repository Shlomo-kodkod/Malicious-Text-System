import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
import logging
from app import config
from app.fetcher import DAL

logger = logging.getLogger(__name__)

class Processor:
    def __init__(self, data: pd.DataFrame):
        self.__df = data
    
    @staticmethod
    def find_rarest_word(text):
        """Finds the rarest word in a given text string."""
        words = text.split()
        word_counts = pd.Series(words).value_counts()
        return word_counts.idxmin() if not word_counts.empty else None
    
    def rarest_word(self, column: str = "Text"):
        """
        Add a new column to the DataFrame with the rarest word in text field for each row.
        """
        if (self.__df is None) or ("Text" not in self.__df.columns):
            logger.error("DataFrame is empty or 'Text' column is missing.")
        self.__df["rarest_word"] = self.__df[column].apply(Processor.find_rarest_word)
        logger.info("successfully find the rarest word per row.")

    @staticmethod
    def calculate_sentiment_score(text: str) -> float:
        """
        Analyzes the sentiment of a given text string and returns a sentiment score.
        """
        score= SentimentIntensityAnalyzer().polarity_scores(text)
        result = score["compound"]
        logger.info(f"Successfully calculated sentiment score.")
        if result >= 0.5: return "positive"
        elif -0.49 < result <= 0.49: return "negative"
        else: return "neutral"

    def analyze_sentiment(self, column: str = "Text"):
        """
        Add a new column to the DataFrame with sentiment scores for each row.
        """
        if (self.__df is None) or (column not in self.__df.columns):
            logger.error("DataFrame is empty or specified column is missing.")
        self.__df["sentiment"] = self.__df[column].apply(Processor.calculate_sentiment_score)
        logger.info("Successfully analyzed sentiment per row.")

    @staticmethod
    def load_blacklist(file_path: str) -> list:
        """
        Load a blacklist of weapons from data and return set of weapons.
        """
        try:
            with open(file_path, 'r') as file:
                blacklist = list(file.read().splitlines())
            logger.info("Blacklist loaded successfully.")
            return blacklist
        except Exception as e:
            logger.error(f"Failed to load blacklist: {e}")
            raise e
    
    @staticmethod
    def find_weapons(text: str, weapons: list):
        """
        Find weapons in the given text using the provided set of weapons.
        """
        found_weapons = [weapon for weapon in weapons if weapon in text]
        return found_weapons[0] if found_weapons else None
    
    def weapons_detector(self, column: str = "Text"):
        """
        Add a new column to the DataFrame with detected weapons for each row.
        """
        if (self.__df is None) or (column not in self.__df.columns):
            logger.error("DataFrame is empty or specified column is missing.")
        weapons = self.load_blacklist(config.blacklist_path)
        self.__df["detected_weapons"] = self.__df[column].apply(lambda x: Processor.find_weapons(x, weapons))
        logger.info("Successfully detected weapons per row.")


    @property
    def get_df(self):
        """
        Get the DataFrame containing the processed data.
        """
        return self.__df
        
     
        

    

        
    

    

