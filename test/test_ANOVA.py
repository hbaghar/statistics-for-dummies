import unittest
from backend.hypothesis_test_handler import ANOVA
from io import BytesIO
import streamlit as st
from src.backend.data_manipulation import DataFrameHandler

class TestANOVA(unittest.TestCase):

    def test_anova_calculation(self):
        
        # Make dataframehandler
        ufr = None
        filepath="datasets/iris.csv"
        with open(filepath, "rb") as fh:
            buf = BytesIO(fh.read())
            ufr = st.uploaded_file_manager.UploadedFileRec(1,"Name", "text/csv", buf.getvalue())
        uf = st.uploaded_file_manager.UploadedFile(ufr)

        # Create our inputs
        df_obj = DataFrameHandler(uf)
        inputs = dict()
        inputs["cat"] = "Species"
        inputs["numeric_col"] = "SepalLengthCm"
        inputs["significance_level"] = 0.05

        # Make ANOVA object
        aov = ANOVA(data_handler=df_obj, **inputs)

        # Perform calculations
        dic = aov.perform_test()

        # separate our values we want to verify
        p = dic["p_value"]
        f = dic["f_value"]
        var_bet = dic["var_between"]
        var_wit = dic["var_within"]
        df_bet = dic["df_between"]
        df_wit = dic["df_within"]
        df_tot = dic["df_total"]
        ss_bet = dic["ss_between"]
        ss_wit = dic["ss_within"]
        ss_tot = dic["ss_total"]
        accept = dic["accept"]

        # unit testing time (used iris dataset in Rstudio to compare)
        self.assertAlmostEqual(p, 0)
        self.assertAlmostEqual(f, 119.3, places=1)
        self.assertAlmostEqual(var_bet, 31.606, places=3)
        self.assertAlmostEqual(var_wit, 0.265, places=1)
        self.assertAlmostEqual(ss_bet, 63.21, places=1)
        self.assertAlmostEqual(ss_wit, 38.96, places=1)
        self.assertAlmostEqual(ss_tot, 63.21+38.96, places=1)
        self.assertAlmostEqual(accept,1)

if __name__ == '__main__':
    unittest.main()