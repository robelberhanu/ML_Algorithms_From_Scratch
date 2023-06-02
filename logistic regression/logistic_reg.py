import numpy as np

class LogisticRegression:

    def __init__(self, lr=0.001, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    # this function is designed to train the model using gradient decent. X and Y represent np arrays of training samples and label samples respectively.
    def fit(self, X, y):
        n_samples, n_fearures = X.shape
        self.weights = np.zeros(n_fearures)
        self.bias = 0

        # gradient decent
        for _ in range(self.n_iters):

            # Define the model
            linear_model = np.dot(X, self.weights) + self.bias
            y_predicted = self._sigmoid(linear_model)

            # update the weight parameters
            dw = (1/ n_samples) * np.dot(X.T, (y_predicted - y)) # derivative with respect to weights
            db = (1 / n_samples) * np.sum(y_predicted - y) # derivative with respect to biases

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

        

    def predict(self, X):
        pass

    # Helper function - sigmoid

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
