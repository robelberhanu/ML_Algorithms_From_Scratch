import numpy as np
from sklearn import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

from naive_bayes import  NaiveBayes

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred)/len(y_true)
    return accuracy