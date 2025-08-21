import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
import logging
from fetcher import DAL

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
    
    def rarest_word(self, column: str = 'Text'):
        """
        Add a new column to the DataFrame with the rarest word in text field for each row of the original DataFrame.
        """
        if (self.__df is None) or ('Text' not in self.__df.columns):
            logger.error("DataFrame is empty or 'Text' column is missing.")
        self.__df['rarest_word'] = self.__df[column].apply(Processor.find_rarest_word)
        logger.info("successfully find the rarest word per row.")

    @staticmethod
    def calculate_sentiment_score(text: str) -> float:
        """
        Analyzes the sentiment of a given text string and returns a sentiment score.
        """
        score= SentimentIntensityAnalyzer().polarity_scores(text)
        result = score['compound']
        logger.info(f"Successfully calculated sentiment score.")
        if result >= 0.5: return 'positive'
        elif -0.49 < result <= 0.49: return 'negative'
        else: return 'neutral'

    def analyze_sentiment(self, column: str = 'Text'):
        """
        Add a new column to the DataFrame with sentiment scores for each row of the original DataFrame.
        """
        if (self.__df is None) or (column not in self.__df.columns):
            logger.error("DataFrame is empty or specified column is missing.")
        self.__df["sentiment"] = self.__df[column].apply(Processor.calculate_sentiment_score)
        logger.info("Successfully analyzed sentiment per row.")
        print(self.__df)
    

        
    

    

d = DAL()
d.connect()
d.read_collection()
d.disconnect()
df = d.get_df
p = Processor(df)
p.rarest_word()
p.analyze_sentiment()
