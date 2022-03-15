import unittest
<<<<<<< HEAD
from backend.hypothesis_test_handler import TTest
import backend.data_manipulation as dm
from io import BytesIO
import streamlit as st
from src.backend.data_manipulation import DataFrameHandler
=======
from backend.hypothesis_tests import t_test_1_samp
from backend.hypothesis_tests import t_test_2_samp_equal_var
from backend.hypothesis_tests import t_test_welch
from sklearn import datasets
import pandas as pd
>>>>>>> 8877d75b2f22077250dacbabb0ea1e54f65413f7

class TestTTest(unittest.TestCase):

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

    def test_t_test_1_sample(self):
        
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
        inputs["equal_var"] = 1
        inputs["significance_level"] = 0.05

        # Make ttest object
        tt1 = TTest(data_handler=df_obj, **inputs)

        # Perform calculations
        dic = tt1.perform_test()

=======
        # import datasets
        iris = datasets.load_iris()
        s_length = pd.DataFrame(iris.data[:,0])
        s_width = pd.DataFrame(iris.data[:, 1])
        p_length = pd.DataFrame(iris.data[:, 2])
        p_width = pd.DataFrame(iris.data[:, 3])

        # call our function
        dic = t_test_1_samp(s_length, 5)

>>>>>>> 8877d75b2f22077250dacbabb0ea1e54f65413f7
        # separate our values we want to verify
        p = dic['p_value']
        t = dic['t_value']
        con_1 = dic['con_low']
        con_2 = dic['con_up']
        samp_mean = dic['sample_mean_1']
        accept = dic['accept']

        # unit testing time (used iris dataset in Rstudio to compare)
        self.assertAlmostEqual(p,0)
        self.assertAlmostEqual(t,12.473, places=3)
        self.assertAlmostEqual(con_1, 5.709, places=2)
        self.assertAlmostEqual(con_2, 5.9769, places=2)
        self.assertAlmostEqual(samp_mean, 5.843, places=3)
        self.assertEqual(accept, 1)

    def test_2_sample_t_test_equal(self):
      
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
        inputs["equal_var"] = 1
        inputs["significance_level"] = 0.05

        # Make ttest object
        tt1 = TTest(data_handler=df_obj, **inputs)

        # Perform calculations
        dic = tt1.perform_test()
=======
        # import datasets
        iris = datasets.load_iris()
        s_length = pd.DataFrame(iris.data[:,0])
        s_width = pd.DataFrame(iris.data[:, 1])
        p_length = pd.DataFrame(iris.data[:, 2])
        p_width = pd.DataFrame(iris.data[:, 3])

        # call our function
        dic = t_test_2_samp_equal_var(p_length, s_length)
>>>>>>> 8877d75b2f22077250dacbabb0ea1e54f65413f7

        # separate our values we want to verify
        p = dic['p_value']
        t = dic['t_value']
        con_1 = dic['con_low']
        con_2 = dic['con_up']
        samp_mean_1 = dic['sample_mean_1']
        samp_mean_2 = dic['sample_mean_2']
        accept = dic['accept']

        # unit testing time (used iris dataset in Rstudio to compare)
        self.assertAlmostEqual(p, 0)
<<<<<<< HEAD
        self.assertAlmostEqual(t, -39.493, places=1)
        self.assertAlmostEqual(con_1, -2.938597, places=2)
        self.assertAlmostEqual(con_2, -2.6574, places=2)
        self.assertAlmostEqual(samp_mean_1, 1.462, places=2)
        self.assertAlmostEqual(samp_mean_2, 4.26, places=2)
        self.assertEqual(accept, 1)

    def test_2_sample_t_test_unequal(self):

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
        inputs["equal_var"] = 1
        inputs["significance_level"] = 0.05

        # Make ttest object
        tt1 = TTest(data_handler=df_obj, **inputs)

        # Perform calculations
        dic = tt1.perform_test()
=======
        self.assertAlmostEqual(t, -13.098, places=3)
        self.assertAlmostEqual(con_1, -2.398643, places=2)
        self.assertAlmostEqual(con_2, -1.772023, places=2)
        self.assertAlmostEqual(samp_mean_1, 3.758, places=3)
        self.assertAlmostEqual(samp_mean_2, 5.843, places=3)
        self.assertEqual(accept, 1)

    def test_2_sample_t_test_unequal(self):
        # import datasets
        iris = datasets.load_iris()
        s_length = pd.DataFrame(iris.data[:,0])
        s_width = pd.DataFrame(iris.data[:, 1])
        p_length = pd.DataFrame(iris.data[:, 2])
        p_width = pd.DataFrame(iris.data[:, 3])

        # call our function
        dic = t_test_welch(p_length, s_length)
>>>>>>> 8877d75b2f22077250dacbabb0ea1e54f65413f7

        # separate our values we want to verify
        p = dic['p_value']
        t = dic['t_value']
        con_1 = dic['con_low']
        con_2 = dic['con_up']
        samp_mean_1 = dic['sample_mean_1']
        samp_mean_2 = dic['sample_mean_2']
        accept = dic['accept']

        # unit testing time (used iris dataset in Rstudio to compare)
        self.assertAlmostEqual(p, 0)
<<<<<<< HEAD
        self.assertAlmostEqual(t, -39.493, places=1)
        self.assertAlmostEqual(con_1, -2.939, places=2)
        self.assertAlmostEqual(con_2, -2.656, places=2)
        self.assertAlmostEqual(samp_mean_1, 1.462, places=2)
        self.assertAlmostEqual(samp_mean_2, 4.26, places=2)
=======
        self.assertAlmostEqual(t, -13.098, places=3)
        self.assertAlmostEqual(con_1, -2.398643, places=2)
        self.assertAlmostEqual(con_2, -1.772023, places=2)
        self.assertAlmostEqual(samp_mean_1, 3.758, places=3)
        self.assertAlmostEqual(samp_mean_2, 5.843, places=3)
>>>>>>> 8877d75b2f22077250dacbabb0ea1e54f65413f7
        self.assertEqual(accept, 1)



if __name__ == '__main__':
    unittest.main()