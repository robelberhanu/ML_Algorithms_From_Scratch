# This class contains test data samples for training.

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
from logistic_reg import LogisticRegression

bc = datasets.load_breast_cancer() # load breast cancer dataset from sklearn
X, y = bc.data, bc.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# utility function to calculate the accuracy of model performance
def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred)/ len(y_true)
    return accuracy


print("LR classification accuracy", accuracy(y_test, predictions))




