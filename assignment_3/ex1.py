# Importing required libraries
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import metrics
import matplotlib.pyplot as plt

# Loading data from CSV file
df = pd.read_csv('weight-height.csv')

# Preparing the data for model training (assuming 'height' and 'weight' columns exist)
x = np.array(df[['height']])  # Features (Height)
y = np.array(df['weight'])    # Target (Weight)

# Calculating the mean of height and weight for reference
xMean = np.mean(x)
yMean = np.mean(y)

# Creating and training the linear regression model
model = linear_model.LinearRegression()
model.fit(x, y)

# Using the model to make predictions
yhat = model.predict(x)

# Plotting the actual data points and the regression line
plt.scatter(x, y, label="Actual Data", alpha=.5)  # Actual data points
# Mean of the data (for reference)
plt.scatter(xMean, yMean, color='red', label="Mean Point")
# Predicted regression line
plt.plot(x, yhat, color="blue", label="Regression Line")
plt.title("Height vs Weight Regression")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.legend()
plt.show()

# Evaluating the performance of the model using RMSE and R-squared (R2)
# Root Mean Squared Error (RMSE)
rmse = np.sqrt(metrics.mean_squared_error(y, yhat))
r2 = metrics.r2_score(y, yhat)  # R-squared (R2) value
print(f"RMSE: {rmse}, R2: {r2}")
