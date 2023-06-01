import numpy as np

class LogisticRegression:

    def __init__(self, lr=0.001, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    # this function is designed to train the model using gradient decent. X and Y represent np arrays of training samples and label samples respectively.
    def fit(self, X, Y):
        pass

    def predict(self, X)