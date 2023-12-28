import numpy as np

class LinearRegression:
    def __init__(self, lr=0.01, n_iters=1000):
        self.lr = lr  # learning rate, determines the step size at each iteration while moving toward a minimum
        self.n_iters = n_iters  # number of iterations for gradient descent
        self.weights = None  # weights/coefficients for the features, will be initialized during fitting
        self.bias = None  # bias/intercept, will be initialized during fitting

    def fit(self, X, y):
        '''
        Fit the linear regression model to the training data using gradient descent.
        
        Parameters:
            X : array-like, shape (n_samples, n_features)
                Training data
            y : array_like, shape (n_samples,)
                Target values
        '''

        # initialize parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)  # initial weights are set to 0 for each feature
        self.bias = 0  # initial bias is set to 0

        # Gradient descent loop
        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + self.bias  # calculate the current prediction

            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))  # derivative with respect to weights
            db = (1 / n_samples) * np.sum(y_predicted - y)  # derivative with respect to bias

            # Update parameters
            self.weights -= self.lr * dw  # update weights
            self.bias -= self.lr * db  # update bias

    def predict(self, X):
        '''
        Predict using the linear model.

        Parameters:
            X : array-like, shape (n_samples, n_features)
                Samples for which to predict

        Returns:
            y_predicted : array, shape (n_samples,)
                Predicted values
        '''

        # Calculate the predicted values
        y_predicted = np.dot(X, self.weights) + self.bias
        return y_predicted
