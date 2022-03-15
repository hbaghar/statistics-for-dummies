import unittest
from backend.hypothesis_tests import t_test_1_samp
from backend.hypothesis_tests import t_test_2_samp_equal_var
from backend.hypothesis_tests import t_test_welch
from sklearn import datasets
import pandas as pd

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
        
        # import datasets
        iris = datasets.load_iris()
        s_length = pd.DataFrame(iris.data[:,0])
        s_width = pd.DataFrame(iris.data[:, 1])
        p_length = pd.DataFrame(iris.data[:, 2])
        p_width = pd.DataFrame(iris.data[:, 3])

        # call our function
        dic = t_test_1_samp(s_length, 5)

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
      
        # import datasets
        iris = datasets.load_iris()
        s_length = pd.DataFrame(iris.data[:,0])
        s_width = pd.DataFrame(iris.data[:, 1])
        p_length = pd.DataFrame(iris.data[:, 2])
        p_width = pd.DataFrame(iris.data[:, 3])

        # call our function
        dic = t_test_2_samp_equal_var(p_length, s_length)

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
        self.assertAlmostEqual(t, -13.098, places=3)
        self.assertAlmostEqual(con_1, -2.398643, places=2)
        self.assertAlmostEqual(con_2, -1.772023, places=2)
        self.assertAlmostEqual(samp_mean_1, 3.758, places=3)
        self.assertAlmostEqual(samp_mean_2, 5.843, places=3)
        self.assertEqual(accept, 1)



if __name__ == '__main__':
    unittest.main()