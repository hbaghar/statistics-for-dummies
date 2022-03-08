from backend import hypothesis_tests as ht
class HypothesisTests(object):
    def __init__(self, **kwargs):
        
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

    def perform_test(self):
        pass

class TTest(HypothesisTests):

    def __init__(self, **kwargs):
        #Identify arguments that are specific to child class and pass the rest to super class __init__
        self.num_samples = kwargs.pop('num_samples', None)
        self.equal_var = kwargs.pop('equal_var', None)
        super().__init__(**kwargs)
    
    def perform_test(self):
        if self.num_samples == "One sample":
            x = self.data_handler.df[self.numeric_col]
            self.results = ht.t_test_1_samp(x, self.mu, self.sig)
        else:
            if self.equal_var:
                slice_dict = self.dh.slice_by_column(self.numeric_col, self.cat, cat1 = self.cat1, cat2 = self.cat2)
                self.results = ht.t_test_welch(slice_dict[self.cat1], slice_dict[self.cat2], self.sig)
            else:
                self.results = ht.t_test_2_samp_equal_var(self.x, self.y, self.sig)
        
            self.results['NaN_found'] = slice_dict['NaN_found']
        return self.results

class ZTest(HypothesisTests):
    
    def __init__(self, **kwargs):
        self.num_samples = kwargs.pop('num_samples', None)
        super().__init__(**kwargs)
    
    def perform_test(self):
        pass

class ANOVA(HypothesisTests):

    def __init__(self, **kwargs):
        self.numeric_column = kwargs.pop('numeric_column', None)
        self.categorical_column = kwargs.pop('categorical_column', None)
        super().__init__(**kwargs)

    def perform_test(self):
        pass
