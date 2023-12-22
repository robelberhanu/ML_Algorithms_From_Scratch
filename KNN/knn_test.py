# Import necessary libraries
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from knn import KNN  # Make sure knn.py is in the same directory or the path is set

# Set up color map for visualizing the classes
cmap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# Load the Iris dataset from sklearn
iris = datasets.load_iris()
X, y = iris.data, iris.target  # X is the feature matrix, y is the target vector

# Split the data into training and testing sets with 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# Print shapes and first entries of the training set for verification
print(X_train.shape)
print(X_train[0])
print(y_train.shape)
print(y_train)

# Create a scatter plot of the dataset, coloring by class and using two of the features
plt.figure()
plt.scatter(X[:, 2], X[:, 3], c=y, cmap=cmap, edgecolor='k', s=20)
plt.show()

# Initialize the KNN classifier with k=3
clf = KNN(k=3)
# Fit the classifier to the training data
clf.fit(X_train, y_train)
# Predict the labels of the test data
predictions = clf.predict(X_test)

# Calculate and print the accuracy of the classifier
acc = np.sum(predictions == y_test) / len(y_test)
print(acc)
