from io import BytesIO

import pandas as pd
import streamlit as st


class DataFrameHandler(object):
    """
    Factory method for creating a DataFrameHandler object that handles the input file to create a dataframe for API use. 
    """
    def __init__(self, file):
        self.df = self.get_dataframe(file)

    def get_dataframe(self, file):
        """
        Returns dataframe from different file types

        Parameters
        ----------
                file (UploadedFile): A UploadedFile object containing a BytesIO file-type that must be CSV, XLS, XLSX or simple JSON.

        Returns:
                (DataFrame): A DataFrame with accessible data recieved in file
        For more information regarding data types visit: https://www.ibm.com/docs/en/wkc/cloud?topic=catalog-previews
        """
        if file.type == "text/csv" or file.type == "application/vnd.ms-excel":
            return pd.read_csv(file)
        elif (
            file.type
            == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ):
            return pd.read_excel(file)
        # Processes only simple JSON, doesn't admit JSON with nested lists inside
        elif file.type == "application/json":
            return pd.read_json(file)
        else:
            print("File type not recognized")

    def get_numeric_columns(self):
        """
        Returns list with names of the numeric columns in the dataframe

        Parameters
        ----------
                df (DataFrame): DataFrame from the DataFrameHandler
        """
        numerics = ["int16", "int32", "int64", "float16", "float32", "float64"]
        return list(self.df.select_dtypes(include=numerics).columns)

    def get_categorical_columns(self):
        """
        Returns list with names of the categorical columns in the dataframe
        There can be numeric columns that are categorical, we will assume that more than 10 unique values is the threshold between categorical and numeric features

        Parameters
        ----------
                df (DataFrame): DataFrame from the DataFrameHandler
        """
        numerics = ["int16", "int32", "int64", "float16", "float32", "float64"]
        num_unique = self.df.nunique()
        less_than_10 = num_unique < 10
        less_than_10_columns = list(
            self.df.filter(less_than_10.index[less_than_10], axis=1).columns
        )
        non_numeric_columns = list(self.df.select_dtypes(exclude=numerics).columns)
        categorical_columns = list(set(less_than_10_columns + non_numeric_columns))
        return categorical_columns

    def get_column_categories(self, category):
        """
        Returns unique list of column categories 

        Parameters
        ----------
                category (String): Name of the categorical column to consider
                df (DataFrame): DataFrame from the DataFrameHandler
        """
        return list(self.df[category].unique())

    def get_descriptive_stats(self):
        """
        Returns the descriptive statistics of numeric columns of the dataframe
        
        Parameters
        ----------
                df (DataFrame): DataFrame from the DataFrameHandler
        """
        return self.df.describe()

    def get_categorical_stats(self):
        """
        Returns the descriptive statistic of categorical columns of the dataframe
        
        Parameters
        ----------
                df (DataFrame): DataFrame from the DataFrameHandler
        """
        return self.df[self.get_categorical_columns()].describe(include="all")

    def get_missing_value_stats(self):
        """
        Returns a string with the amount of missing values in each column inside the dataframe.
        
        Parameters
        ----------
                df (DataFrame): DataFrame from the DataFrameHandler
        """
        return self.df.isnull().sum()

    def slice_by_column(self, categorical_column, numeric_column, **kwargs):
        """
        Returns dictionary with Series objects from the numeric_column each sliced by their respective grouping in the categorical_column.
        If there are NaN in the categorical_column we don't consider them

        Parameters
        ----------
                categorical_column (String): Name of the categorical column that contains the grouping for slicing
                numeric_column (String): Name of the numerical column that contains the values that are to be sliced

        Returns:
                (Dictionary): A Dictionary containing numerical Series from the slicing performed, if NaN we remove them
        """
        grouped_dict = {}
        grouped_dict["cat_NaN_found"] = False
        grouped_dict["num_NaN_found"] = False
        if self.df[categorical_column].isnull().values.any():
            grouped_dict["cat_NaN_found"] = True
        if self.df[numeric_column].isnull().values.any():
            grouped_dict["num_NaN_found"] = True
        temp_df = self.df.dropna(subset=[categorical_column, numeric_column], how="any")

        categories = temp_df[categorical_column].unique()
        grouped = temp_df.groupby(categorical_column)

        if kwargs != {}:
            for key, value in kwargs.items():
                grouped_dict[value] = grouped.get_group(value)[numeric_column]
        else:
            for i in range(len(categories)):
                temp = grouped.get_group(categories[i])[numeric_column]
                grouped_dict[categories[i]] = temp
        return grouped_dict


if __name__ == "__main__":
    ufr = None
    filepath = "datasets/biostats.csv"
    with open(filepath, "rb") as fh:

        buf = BytesIO(fh.read())
        ufr = st.uploaded_file_manager.UploadedFileRec(
            1, "Name", "text/csv", buf.getvalue()
        )

    uf = st.uploaded_file_manager.UploadedFile(ufr)
    obj = DataFrameHandler(uf)
    print(obj.slice_by_column("Sex", "Age", cat1="F", cat2="M", cat3="T"))