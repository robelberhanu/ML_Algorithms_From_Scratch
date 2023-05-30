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

        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + bias 

            dw = (1/n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1/n_samples) * np.sum(y_predicted - y)
    
    def predict(self, X):
        y_predicted = np.dot(X, self.weights) + bias 
        return y_predicted

            


          



        