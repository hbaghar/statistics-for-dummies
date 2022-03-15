import unittest
<<<<<<< HEAD
from backend.hypothesis_test_handler import ZTest
from io import BytesIO
import streamlit as st
from src.backend.data_manipulation import DataFrameHandler
=======
from backend.hypothesis_tests import z_test_1_samp
from backend.hypothesis_tests import z_test_2_samp
from sklearn import datasets
import pandas as pd
>>>>>>> 8877d75b2f22077250dacbabb0ea1e54f65413f7

class TestZTest(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_z_test_1_sample(self):

<<<<<<< HEAD
        # Make dataframehandler
        ufr = None
        filepath="datasets/iris.csv"
        with open(filepath, "rb") as fh:
            buf = BytesIO(fh.read())
            ufr = st.uploaded_file_manager.UploadedFileRec(1,"Name", "text/csv", buf.getvalue())
        uf = st.uploaded_file_manager.UploadedFile(ufr)
        df_obj = DataFrameHandler(uf)

        # Create our inputs
        inputs = dict()
        inputs["cat"] = "Species"
        inputs["numeric_col"] = "SepalLengthCm"
        inputs["cat1"] = None
        inputs["cat2"] = None
        inputs["mu"] = 5
        inputs["num_samples"] = "One sample"
        inputs["significance_level"] = 0.05

        # Make ttest object
        zt1 = ZTest(data_handler=df_obj, **inputs)

        # Perform calculations
        dic = zt1.perform_test()
=======
        # import datasets
        iris = datasets.load_iris()
        s_length = pd.DataFrame(iris.data[:,0])
        s_width = pd.DataFrame(iris.data[:, 1])
        p_length = pd.DataFrame(iris.data[:, 2])
        p_width = pd.DataFrame(iris.data[:, 3])

        # call our function
        dic = z_test_1_samp(s_length, 5)
>>>>>>> 8877d75b2f22077250dacbabb0ea1e54f65413f7

        # separate our values we want to verify
        p = dic['p_value']
        z = dic['z_value']
        con_1 = dic['con_low']
        con_2 = dic['con_up']
        samp_mean_1 = dic['sample_mean_1']
        accept = dic['accept']

        # unit testing time (used iris dataset in Rstudio to compare)
        self.assertAlmostEqual(p, 0)
        self.assertAlmostEqual(z, 12.473, places=3)
        self.assertAlmostEqual(con_1, 5.7108, places=2)
        self.assertAlmostEqual(con_2, 5.975879, places=2)
        self.assertAlmostEqual(samp_mean_1, 5.843, places=3)
        self.assertEqual(accept, 1)

    def test_z_test_2_sample(self):

<<<<<<< HEAD
        # Make dataframehandler
        ufr = None
        filepath="datasets/iris.csv"
        with open(filepath, "rb") as fh:
            buf = BytesIO(fh.read())
            ufr = st.uploaded_file_manager.UploadedFileRec(1,"Name", "text/csv", buf.getvalue())
        uf = st.uploaded_file_manager.UploadedFile(ufr)
        df_obj = DataFrameHandler(uf)

        # Create our inputs
        inputs = dict()
        inputs["cat"] = "Species"
        inputs["numeric_col"] = "PetalLengthCm"
        inputs["cat1"] = "Iris-setosa"
        inputs["cat2"] = "Iris-versicolor"
        inputs["mu"] = 5
        inputs["num_samples"] = "Two sample"
        inputs["significance_level"] = 0.05

        # Make ttest object
        zt1 = ZTest(data_handler=df_obj, **inputs)

        # Perform calculations
        dic = zt1.perform_test()
=======
        # import datasets
        iris = datasets.load_iris()
        s_length = pd.DataFrame(iris.data[:,0])
        s_width = pd.DataFrame(iris.data[:, 1])
        p_length = pd.DataFrame(iris.data[:, 2])
        p_width = pd.DataFrame(iris.data[:, 3])

        # call our function
        dic = z_test_2_samp(s_length, p_length)
>>>>>>> 8877d75b2f22077250dacbabb0ea1e54f65413f7

        # separate our values we want to verify
        p = dic['p_value']
        z = dic['z_value']
        con_1 = dic['con_low']
        con_2 = dic['con_up']
        samp_mean_1 = dic['sample_mean_1']
        samp_mean_2 = dic['sample_mean_2']
        accept = dic['accept']

        # unit testing time (used iris dataset in Rstudio to compare)
        self.assertAlmostEqual(p, 0)
<<<<<<< HEAD
        self.assertAlmostEqual(z, -39.493, places=1)
        self.assertAlmostEqual(con_1, -2.9368, places=2)
        self.assertAlmostEqual(con_2, -2.659, places=2)
        self.assertAlmostEqual(samp_mean_1, 1.462, places=2)
        self.assertAlmostEqual(samp_mean_2, 4.26, places=2)
=======
        self.assertAlmostEqual(z, 13.098, places=3)
        self.assertAlmostEqual(con_1, 1.77, places=2)
        self.assertAlmostEqual(con_2, 2.397, places=2)
        self.assertAlmostEqual(samp_mean_1, 5.843, places=3)
        self.assertAlmostEqual(samp_mean_2, 3.758, places=3)
>>>>>>> 8877d75b2f22077250dacbabb0ea1e54f65413f7
        self.assertEqual(accept, 1)


if __name__ == '__main__':
    unittest.main()