import pandas as pd
from io import BytesIO
import streamlit as st
class DataFrameHandler(object):

    def __init__(self, file):
        print("Init of df-handler has executed")
        self.df = self.get_dataframe(file)
    
    def get_dataframe(self, file):
        '''
            Returns dataframe from different file types

            Parameters:
                    file (UploadedFile): A UploadedFile object containing a BytesIO file-type that must be CSV, XLS, XLSX or simple JSON.
                    
            Returns:
                    (DataFrame): A DataFrame with accessible data recieved in file
            For more information regarding data types visit: https://www.ibm.com/docs/en/wkc/cloud?topic=catalog-previews
        '''
        if file.type == 'text/csv':
            return pd.read_csv(file)
        elif file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.type == 'application/vnd.ms-excel' :
            return pd.read_excel(file)
        #Processes only simple JSON, doesn't admit JSON with nested lists inside
        elif file.type == 'application/json':
            return pd.read_json(file)

    def get_numeric_columns(self):
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        return self.df.select_dtypes(include=numerics).columns

    def get_categorical_columns(self):
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        return self.df.select_dtypes(exclude=numerics).columns
    
    def get_descriptive_stats(self):
        return self.df.describe()

    def get_categorical_stats(self):
        return self.df[self.get_categorical_columns()].describe(include='all')

    def get_missing_value_stats(self):
        return self.df.isnull().sum()

    def slice_by_column(self, categorical_column, numeric_column):
        #TO-DO:
        # - Phase 1: Split by all categories in a column
        # - Phase 2: Split by specific categories in a column (?)
        pass
    

if __name__ == "__main__":
    ufr=None    
    filepath = 'biostats.csv'
    with open(filepath, 'rb') as fh:
        
        buf = BytesIO(fh.read())
        ufr=st.uploaded_file_manager.UploadedFileRec(1,'Name','text/csv',buf.getvalue())
    
    uf = st.uploaded_file_manager.UploadedFile(ufr)
    obj = DataFrameHandler(uf)
    print(obj.get_missing_value_stats())


#uploaded_file = st.file_uploader("Choose a CSV file")
#print(uploaded_file.type)

