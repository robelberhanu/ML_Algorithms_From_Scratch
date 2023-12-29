import numpy as np
# Importing the numpy library to handle numerical operations

class NaiveBayes:
    # Defining a class for the Naive Bayes classifier

    def fit(self, X, y):
        # 'fit' method to train the model on data X and labels y
        n_samples, n_features = X.shape  # Number of samples and features in the dataset
        self.__classes = np.unique(y)  # Unique classes in the target variable
        n_classes = len(self.__classes)  # Number of unique classes

        # Initializing mean, variance, and priors for each class
        self._mean = np.zeros((n_classes, n_features), dtype=np.float64)
        self._var = np.zeros((n_classes, n_features), dtype=np.float64)
        self.__priors = np.zeros(n_classes, dtype=np.float64)

        for c in self.__classes:
            # Calculating mean, variance, and prior for each class
            X_c = X[c==y]  # Filter samples for the class c
            self._mean[c,:] = X_c.mean(axis=0)  # Calculate mean for class c
            self._var[c,:] = X_c.var(axis=0)  # Calculate variance for class c
            self.__priors[c] = X_c.shape[0] / float(n_samples)  # Calculate prior probability for class c

    def predict(self, X):
        # 'predict' method to predict the class for given data X
        y_pred = [self._predict(x) for x in X]  # List comprehension to predict for each sample
        return y_pred
    
    def _predict(self, x):
        # Helper method to compute the class with the highest posterior probability for a given sample x
        posteriors = []

        for idx, c in enumerate(self.__classes):
            # Calculating the posterior probability for each class
            prior = np.log(self.__priors[idx])  # Log of the prior probability
            class_conditional = np.sum(np.log(self._pdf(idx, x)))  # Log of the likelihood
            posterior = prior + class_conditional  # Log posterior is the sum of log prior and log likelihood
            posteriors.append(posterior)
        
        return self.__classes[np.argmax(posteriors)]
        # Returning the class with the highest posterior probability

    def _pdf(self, class_idx, x):
        # Helper method to calculate the probability density function of a normal distribution
        mean = self._mean[class_idx]
        var = self._var[class_idx]
        numerator = np.exp(- (x-mean)**2 / (2 * var))  # Calculating the numerator of the Gaussian formula
        denominator = np.sqrt(2 * np.pi * var)  # Calculating the denominator of the Gaussian formula
        return numerator / denominator
