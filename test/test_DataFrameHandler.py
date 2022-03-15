import unittest
from backend.data_manipulation import DataFrameHandler
from io import BytesIO
import streamlit as st

class TestDataFrameHandler(unittest.TestCase):

    def test_get_num_col(self):

        # Make dataframehandler
        ufr = None
        filepath="datasets/iris.csv"
        with open(filepath, "rb") as fh:
            buf = BytesIO(fh.read())
            ufr = st.uploaded_file_manager.UploadedFileRec(1,"Name", "text/csv", buf.getvalue())
        uf = st.uploaded_file_manager.UploadedFile(ufr)

        # Create our inputs
        df_obj = DataFrameHandler(uf)
        
        # Perform calculation
        lst = df_obj.get_numeric_columns()

        # unit testing time
        self.assertEqual(lst[0], "Id")
        self.assertEqual(lst[1], "SepalLengthCm")
        self.assertEqual(lst[2], "SepalWidthCm")
        self.assertEqual(lst[3], "PetalLengthCm")
        self.assertEqual(lst[4], "PetalWidthCm")

    def test_get_cat_col(self):

        # Make dataframehandler
        ufr = None
        filepath="datasets/iris.csv"
        with open(filepath, "rb") as fh:
            buf = BytesIO(fh.read())
            ufr = st.uploaded_file_manager.UploadedFileRec(1,"Name", "text/csv", buf.getvalue())
        uf = st.uploaded_file_manager.UploadedFile(ufr)

        # Create our inputs
        df_obj = DataFrameHandler(uf)
        
        # Perform calculation
        lst = df_obj.get_categorical_columns()

        # unit testing time
        self.assertEqual(lst[0], "Species")

    def test_get_col_cats(self):

        # Make dataframehandler
        ufr = None
        filepath="datasets/iris.csv"
        with open(filepath, "rb") as fh:
            buf = BytesIO(fh.read())
            ufr = st.uploaded_file_manager.UploadedFileRec(1,"Name", "text/csv", buf.getvalue())
        uf = st.uploaded_file_manager.UploadedFile(ufr)

        # Create our inputs
        df_obj = DataFrameHandler(uf)
        
        # Perform calculation
        lst = df_obj.get_column_categories("Species")

        # unit testing time
        self.assertEqual(lst[0], "Iris-setosa")
        self.assertEqual(lst[1], "Iris-versicolor")
        self.assertEqual(lst[2], "Iris-virginica")

if __name__ == '__main__':
    unittest.main()