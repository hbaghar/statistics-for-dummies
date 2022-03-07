class HypothesisTests(object):
    def __init__(self, sig_level, alt_hypothesis, null_hypothesis):
        self.sig_level = sig_level
        self.alt_hypothesis = alt_hypothesis
        self.null_hypothesis = null_hypothesis

        self.pvalue = None
        self.test_statistic = None
        self.test_result = None
        self.confidence_interval = None
    
    def perform_test(self):
        pass

class TTest(HypothesisTests):

    def __init__(self, num_samples, equal_var, **kwargs):
        #Identify arguments that are specific to child class and pass the rest to super class __init__
        super().__init__(**kwargs)
        self.num_samples = num_samples
        self.equal_var = equal_var
    
    def perform_test(self):
        pass

class Ztest(HypothesisTests):
    
    def __init__(self, num_samples, **kwargs):
        super().__init__(**kwargs)
        self.num_samples = num_samples
    
    def perform_test(self):
        pass

class ANOVA(HypothesisTests):

    def __init__(self, categorical_column, numeric_column, **kwargs):
        super().__init__(**kwargs)
        self.categorical_column = categorical_column
        self.numeric_column = numeric_column

    def perform_test(self):
        pass
