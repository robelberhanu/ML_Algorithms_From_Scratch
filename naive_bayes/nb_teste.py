import numpy as np
# Importing the numpy library for numerical operations

from sklearn.model_selection import train_test_split
# Importing train_test_split function to divide the data into training and testing sets

from sklearn import datasets
# Importing datasets from scikit-learn to generate a synthetic dataset

import matplotlib.pyplot as plt
# Importing matplotlib for potential data visualization (not used in this script)

from naive_bayes import NaiveBayes
# Importing the NaiveBayes class you defined earlier

def accuracy(y_true, y_pred):
    # Defining a function to calculate accuracy
    accuracy = np.sum(y_true == y_pred) / len(y_true)  # Calculates the accuracy as the proportion of correct predictions
    return accuracy

# Generating a synthetic dataset with 1000 samples, 10 features, 2 classes, and a fixed random state
X, y = datasets.make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=123)

# Splitting the dataset into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

nb = NaiveBayes()  # Creating an instance of the NaiveBayes class
nb.fit(X_train, y_train)  # Training the NaiveBayes model with the training data
predictions = nb.predict(X_test)  # Predicting the labels of the test data

# Printing the accuracy of the Naive Bayes classifier on the test data
print("Naive Bayes classification accuracy", accuracy(y_test, predictions))
