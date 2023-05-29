import numpy as np


class LinearRegression:
    def __init__(self, lr=0.001, n_iters = 1000):
        self.lr = lr # learning rate
        self.n_iters = n_iters # number of iterationn for gradient decent
        self.weights = None
        self.bias = None

    def fit (self, X, Y):
        '''
        This method deals with the learning process - using gradient decent.
        
        '''

        # initialize parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0;

   

            


          



        