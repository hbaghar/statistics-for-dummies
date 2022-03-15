import unittest
from backend.hypothesis_tests import one_way_anova
from sklearn import datasets
import pandas as pd

class TestANOVA(unittest.TestCase):

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

    def test_anova_calculation(self):
        
        # import datasets
        iris = datasets.load_iris()
        s_length = pd.DataFrame(iris.data[:,0])
        s_width = pd.DataFrame(iris.data[:, 1])
        p_length = pd.DataFrame(iris.data[:, 2])
        p_width = pd.DataFrame(iris.data[:, 3])

        # make our dictionary
        aov_dic = {"Setosa": iris.data[:,0][0:50], "Versicolour": iris.data[:,0][50:100], "Virginica": iris.data[:,0][100:150]}

        # call our function
        dic = one_way_anova(aov_dic)

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