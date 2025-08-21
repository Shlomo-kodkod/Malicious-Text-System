import pandas as pd
import logging
from app.fetcher import DAL
from app.processor import Processor


logger = logging.getLogger(__name__)

class Manager:
    def __init__(self):
        self.__data = None
        self.__dal = DAL()
        self.__processor = None

    def load_data(self) -> pd.DataFrame:
        """
        Load data from the database and return a DataFrame.
        """
        self.__dal.connect()
        self.__dal.read_collection()
        df = self.__dal.get_df
        self.__dal.disconnect()
        return df
    
    def process_data(self):
        """
        Process the DataFrame by finding the rarest word and analyzing sentiment and weapons.
        """ 
        self.__processor = Processor(self.load_data())
        self.__processor.rarest_word()
        self.__processor.analyze_sentiment()
        self.__processor.weapons_detector()
        self.__data = self.__processor.get_df

    

    def get_processed_data(self) -> dict:
        """
        Return the processed aata.
        """
        logger.info("Starting data processing.")
        self.load_data()
        self.process_data()
        if self.__data is None:
            raise ValueError("Data has not been processed yet.")
        logger.info("Data processing completed successfully.")
        return self.__data.to_dict(orient="records")

