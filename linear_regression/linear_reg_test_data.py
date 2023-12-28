# Import necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
from linear_regression.linear_reg import LinearRegression

# Generate a random regression problem with 100 samples, 1 feature, added noise, and a set random state for reproducibility
X, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)

# Split the dataset into training and testing sets with 80% for training and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# The following code is commented out. If enabled, it would create a scatter plot of the data points
# fig = plt.figure(figsize=(8,6))
# plt.scatter(X[:,0], y, color="b", marker="o", s = 30)
# plt.show()

# Create an instance of the LinearRegression class
regressor = LinearRegression()

# Fit the model to the training data
regressor.fit(X_train, y_train)

# Predict the values for the testing data
predicted = regressor.predict(X_test)

# Define a function to calculate the mean squared error between true and predicted values
def mse(y_true, y_predicted):
    return np.mean((y_true - y_predicted)**2)

# Calculate and print the mean squared error for the test data
mse_value = mse(y_test, predicted)
print(mse_value)

# Plotting the model
# Generate predictions across the entire dataset for the line
y_pred_line = regressor.predict(X)

# Set up the color map for the plots
cmap = plt.get_cmap('viridis')

# Initialize a figure for plotting
fig = plt.figure(figsize=(8,6))

# Plot the training data points
m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10)

# Plot the testing data points
m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)

# Plot the prediction line across all data points
plt.plot(X, y_pred_line, color='black', linewidth=2, label='Prediction')

# Display the plot
plt.show()

# The last section of code is repeated and will generate the same plot as above.
