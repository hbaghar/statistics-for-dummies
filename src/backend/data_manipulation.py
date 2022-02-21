import pandas as pd

class DataFrameHandler(object):

    def __init__(self, file):
        self.df = self.get_dataframe(file)
    
    def get_dataframe(self, file):
        # TO-DO:
        # - Write handler for different file types and return dataframe
        pass

    def get_numeric_columns(self):
        pass

    def get_categorical_columns(self):
        pass
    
    def get_descriptive_stats(self):
        pass

    def get_categorial_stats(self):
        pass

    def get_missing_value_stats(self):
        pass

    def slice_by_column(self, categorical_column, numeric_column):
        #TO-DO:
        # - Phase 1: Split by all categories in a column
        # - Phase 2: Split by specific categories in a column (?)
        pass