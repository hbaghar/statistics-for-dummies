import unittest
from io import BytesIO

import streamlit as st

from src.backend.data_manipulation import DataFrameHandler
from src.backend.hypothesis_test_handler import ZTest


class TestZTest(unittest.TestCase):

    def test_z_test_1_sample(self):

        # Make dataframehandler
        ufr = None
        filepath="datasets/Iris.csv"
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

        # Make dataframehandler
        ufr = None
        filepath="datasets/Iris.csv"
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
        self.assertAlmostEqual(z, -39.493, places=1)
        self.assertAlmostEqual(con_1, -2.9368, places=2)
        self.assertAlmostEqual(con_2, -2.659, places=2)
        self.assertAlmostEqual(samp_mean_1, 1.462, places=2)
        self.assertAlmostEqual(samp_mean_2, 4.26, places=2)
        self.assertEqual(accept, 1)


if __name__ == '__main__':
    unittest.main()