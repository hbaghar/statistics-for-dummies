from backend import hypothesis_tests as ht


class HypothesisTests(object):
    """
    Factory method for creating a hypothesis test object. Each test type inherits from this class.
    """
    def __init__(self, **kwargs):

        for arg in kwargs:
            setattr(self, arg, kwargs[arg])
        
        #TODO:
        # - Improve handling of results of tests so that UI can be simpler using below class variables

        self.pvalue = None
        self.test_type = None
        self.test_statistic = None
        self.test_result = None
        self.confidence_interval = None, None

    def perform_test(self):
        """
        Perform the test. Written so that UI code can be simpler and refers simply to one function.
        """
        raise NotImplementedError("This method must be implemented by a subclass.")


class TTest(HypothesisTests):
    """
    Wrapper class for T-Test that calls appropriate function from the hypothesis_tests module.
    
    Parameters
    ----------
    data_handler : DataFrameHandler object to be used on the data.
    cat : str
        Column name of categorical variable.
    numeric_col : str
        Column name of numeric variable.
    cat1 : str
        First category of categorical variable.
    cat2 : str
        Second category of categorical variable.
    mu : float
        Population Mean of the distribution.
    num_samples : str
        Number of samples to be used in the test (one-sample vs two-sample).
    equal_var : bool
        Whether to use equal variance t-test or Welch's t-test with unequal variances.
    significance_level : float
        Significance level to use for hypothesis test.
    """
    def __init__(self, **kwargs):
        # Identify arguments that are specific to child class and pass the rest to super class __init__
        self.num_samples = kwargs.pop("num_samples", None)
        self.equal_var = kwargs.pop("equal_var", None)
        super().__init__(**kwargs)

    def perform_test(self):
        """
        Perform the test. Collects the UI inputs that have been passed and calls apporpriate function from hypothesis_tests module.

        Returns a dictionary containing the results of the test.
        """
        if self.num_samples == "One sample":
            x = self.data_handler.df[self.numeric_col]
            nan_found = x.isnull().values.any()
            x.dropna(inplace=True)
            self.results = ht.t_test_1_samp(x, self.mu, self.significance_level)
            self.results["num_NaN_found"] = nan_found
        else:
            slice_dict = self.data_handler.slice_by_column(
                self.cat, self.numeric_col, cat1=self.cat1, cat2=self.cat2
            )
            if self.equal_var:
                self.results = ht.t_test_welch(
                    slice_dict[self.cat1],
                    slice_dict[self.cat2],
                    self.significance_level,
                )
            else:
                self.results = ht.t_test_2_samp_equal_var(
                    slice_dict[self.cat1],
                    slice_dict[self.cat2],
                    self.significance_level,
                )

            self.results["cat_NaN_found"] = slice_dict["cat_NaN_found"]
            self.results["num_NaN_found"] = slice_dict["num_NaN_found"]
        return self.results


class ZTest(HypothesisTests):
    """
    Wrapper class for Z-Test that calls appropriate function from the hypothesis_tests module.

    Parameters
    ----------
    data_handler : DataFrameHandler object to be used on the data.
    cat : str
        Column name of categorical variable.
    numeric_col : str
        Column name of numeric variable.
    cat1 : str  
        First category of categorical variable.
    cat2 : str
        Second category of categorical variable.
    mu : float
        Population Mean of the distribution.
    num_samples : str
        Number of samples to be used in the test (one-sample vs two-sample).
    significance_level : float
        Significance level to use for hypothesis test.
    """

    def __init__(self, **kwargs):
        self.num_samples = kwargs.pop("num_samples", None)
        super().__init__(**kwargs)

    def perform_test(self):
        """
        Perform the test. Collects the UI inputs that have been passed and calls apporpriate function from hypothesis_tests module.
        """
        if self.num_samples == "One sample":
            x = self.data_handler.df[self.numeric_col]
            nan_found = x.isnull().values.any()
            x.dropna(inplace=True)
            self.results = ht.z_test_1_samp(x, self.mu, self.significance_level)
            self.results["num_NaN_found"] = nan_found
        else:
            slice_dict = self.data_handler.slice_by_column(
                self.cat, self.numeric_col, cat1=self.cat1, cat2=self.cat2
            )
            self.results = ht.z_test_2_samp(
                slice_dict[self.cat1], slice_dict[self.cat2], self.significance_level
            )
            self.results["cat_NaN_found"] = slice_dict["cat_NaN_found"]
            self.results["num_NaN_found"] = slice_dict["num_NaN_found"]
        return self.results


class ANOVA(HypothesisTests):
    """
    Wrapper class for ANOVA that calls appropriate function from the hypothesis_tests module.

    Parameters
    ----------
    data_handler : DataFrameHandler object to be used on the data.
    cat : str
        Column name of categorical variable.
    numeric_col : str
        Column name of numeric variable.
    significance_level : float 
        Significance level to use for hypothesis test.
    """
    def __init__(self, **kwargs):
        self.numeric_col = kwargs.pop("numeric_col", None)
        self.categorical_column = kwargs.pop("categorical_column", None)
        super().__init__(**kwargs)

    def perform_test(self):
        """
        Perform the test. Collects the UI inputs that have been passed and calls apporpriate function from hypothesis_tests module.
        """
        slice_dict = self.data_handler.slice_by_column(self.cat, self.numeric_col)
        # TODO: Handle when number of categorical is equal to number of values (Name)-> Division by 0.
        self.results = ht.one_way_anova(slice_dict, self.significance_level)
        self.results["cat_NaN_found"] = slice_dict["cat_NaN_found"]
        self.results["num_NaN_found"] = slice_dict["num_NaN_found"]

        return self.results
