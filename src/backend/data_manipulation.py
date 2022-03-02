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
        return list(self.df.select_dtypes(include=numerics).columns)

    def get_categorical_columns(self):
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        return list(self.df.select_dtypes(exclude=numerics).columns)
    
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
        '''
            Returns dictionary with Series from the numeric_column each sliced by their respective grouping in the categorical_column.
            If there are NaN in the categorical_column we don't consider them

            Parameters:
                    categorical_column (String): Name of the categorical column that contains the grouping for slicing
                    numeric_column (String): Name of the numerical column that contains the values that are to be sliced
                    
            Returns:
                    (Dictionary): A Dictionary containing numerical Series from the slicing performed and last value contains number of categories
        '''
        grouped_dict={}
        grouped_dict['NaN_found']=False
        if self.df[categorical_column].isnull().values.any():
            grouped_dict['NaN_found']=True
        temp_df=self.df.dropna(subset=[categorical_column])
        categories=temp_df[categorical_column].unique()
        grouped=temp_df.groupby(categorical_column)
        n=len(categories)
        for i in range(len(categories)):
            temp_series=grouped.get_group(categories[i])[numeric_column]
            grouped_dict[categories[i]]=temp_series
        grouped_dict['len']=n
        return grouped_dict
    
    

if __name__ == "__main__":
    ufr=None    
    filepath = 'biostats.csv'
    with open(filepath, 'rb') as fh:
        
        buf = BytesIO(fh.read())
        ufr=st.uploaded_file_manager.UploadedFileRec(1,'Name','text/csv',buf.getvalue())
    
    uf = st.uploaded_file_manager.UploadedFile(ufr)
    obj = DataFrameHandler(uf)
    print(obj.get_categorical_stats())


#uploaded_file = st.file_uploader("Choose a CSV file")
#print(uploaded_file.type)

