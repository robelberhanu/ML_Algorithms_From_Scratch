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

        # gradient decent - update the weight parameters
        for _ in range(self.n_iters):
            dw = (1/ n_samples) * np.dot(X.T, (y_predicted - y)) # derivative with respect to weights
            db = (1 / n_samples) * np.sum(y_predicted - y) # derivative with respect to biases

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

        

    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = self._sigmoid(linear_model)
        y_predicted_cls = [1 if i > 0.5 else 0 for i in y_predicted] # this classifies the predictions based on their value
        return y_predicted_cls
         

    # Helper function - sigmoid
    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
