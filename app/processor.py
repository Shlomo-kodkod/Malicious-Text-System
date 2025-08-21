import pandas as pd


class Processor:
    def __init__(self):
        self.__df = None
    
    @staticmethod
    def find_rarest_word(text):
        """Finds the rarest word in a given text string."""
        words = text.split()
        word_counts = pd.Series(words).value_counts()
        return word_counts.idxmin() if not word_counts.empty else None
    
    def rarest_word_per_row(self, column: str = 'text'):
        """
        Returns a DataFrame with the rarest word in text field for each row of the DataFrame.
        """
        if self._df is None or 'text' not in self.__df.columns:
            return None
        self.__df['rarest_word'] = self.__df[column].apply(Processor.find_rarest_word)
