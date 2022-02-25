import pandas as pd
from io import BytesIO
import streamlit as st
class DataFrameHandler(object):

    def __init__(self, file):
        print("Init of df-handler has executed")
        self.df = self.get_dataframe(file)
    
    def get_dataframe(self, file):
        # TO-DO:
        # - Write handler for different file types and return dataframe
        if file.type == 'text/csv':
            return pd.read_csv(file)

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
    

if __name__ == "__main__":
    ufr=None    
    filepath = 'src/backend/Sales.csv'
    with open(filepath, 'rb') as fh:
        
        buf = BytesIO(fh.read())
        ufr=st.uploaded_file_manager.UploadedFileRec(1,'Hello','text/csv',buf.getvalue())
    
    uf = st.uploaded_file_manager.UploadedFile(ufr)
    obj = DataFrameHandler(uf)


#uploaded_file = st.file_uploader("Choose a CSV file")
#print(uploaded_file.type)

