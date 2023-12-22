import numpy as np
from collections import Counter

# Function to calculate euclidean distance between two points
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))  # Corrected the formula

# KNN classifier
class KNN:

    # Constructor to initialize the KNN object with k neighbors
    def __init__(self, k=3):
        self.k = k

    # Method to fit the classifier with the training data
    def fit(self, X, y):
        self.X_train = X  # Training features
        self.y_train = y  # Training labels

    # Method to predict the class of a given set of samples
    def predict(self, X):
        # Apply _predict to each entry in the dataset X
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)
    
    # Helper method to predict the class of a single sample
    def _predict(self, x):
        # Compute distances between x and all examples in the training set
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]

        # Get the indices of the k nearest neighbors
        k_indices = np.argsort(distances)[:self.k]
        # Extract the labels of the k nearest neighbors
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # Perform a majority vote to find the most common class among the nearest neighbors
        most_common = Counter(k_nearest_labels).most_common(1)

        return most_common[0][0]  # Return the most common class label
