# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
# We have two column in CSV files
# The independent variable column is Years of Experience 
X = dataset.iloc[:, :-1].values
# We need to calculate the dependent variable i.e Salary. Our Y variable is independent variable. Variable of Feature.
# We Import the dataset into variable y. Column Salary.
y = dataset.iloc[:, 1].values

# Simple Linear Regression Theory and Physics
# y = mx + b
# Where we need to calculate y for regressive values of X
# M - is Slope
# b - is Coefficient considering x = 1

# Splitting the dataset into the Training set and Test set
# We can split the available dataset into two sets.
# We can train the module with sample data and then we can request the module to predict the value of independent variable
# for test set.
# X_train Will have few sample values of X to train the module
# X_test Will have few sample value to test the module if results are closer to expected values.
# y_train will be values for trained x_train samples
# y_test are the predicted values of y_test samples - Visa versa - Confusing Yet :P
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
# Fit the best fit line for the available data sample
# This can be done using the mathematical formulae not illustrated at early stages
# Currently we just have an object called regressor
regressor.fit(X_train, y_train)

# Predicting the Test set results
# We are predicting y_test results here
y_pred = regressor.predict(X_test)

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
