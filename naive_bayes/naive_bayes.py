import numpy as np

class NaiveBayes:


    def fit(Self, X, y):
        n_samples, n_features = X.shape
        self._classes = np.unique(y)
        n_classes = len(Self._classes)

        # initialise mean var, priors
        self._mean = np.zeros((n_classes, n_features), dtype=np.float64)
        self._var = np.zeros((n_classes,n_features), dtype=np.float64)

    
    def predict(self, X):
        pass