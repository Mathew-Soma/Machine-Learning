import numpy as np

# Sample data for x and y values
x = np.array([10, 20, 30, 40, 50])
y = np.array([5, 10, 15, 20, 25])

# Calculate the mean of x and y
mean_x = np.mean(x)
mean_y = np.mean(y)

# Calculate the numerator for the slope (b1) using deviations from means
numerator = np.sum((x - mean_x) * (y - mean_y))

# Calculate the denominator for the slope (b1) using squared deviations from mean of x
denominator = np.sum(np.square(x - mean_x))

# Calculate the slope (b1)
slope_b1 = numerator / denominator

# Print the slope (b1) coefficient
print("Slope (b1):", slope_b1)

# Calculate the y-intercept (b0) using the formula with means and slope
y_intercept_b0 = mean_y - slope_b1 * mean_x

# Print the y-intercept (b0) coefficient
print("Y-intercept (b0):", y_intercept_b0)

# Define a function to predict y for a given x value
def predict(value_of_x):
  """
  This function predicts the y value based on the slope (b1) and y-intercept (b0)
  obtained from the linear regression, for a given input x value.
  """
  return y_intercept_b0 + (slope_b1 * value_of_x)

# Continuously prompt user for input until they enter 'quit'
while True:
  user_value = input("Enter x value (or 'quit' to exit): ")

  if user_value.lower() == 'quit':
    break  # Exit the loop if user enters 'quit'

  try:
    # Convert user input to integer
    user_value = int(user_value)

    # Predict y using the defined function
    predicted_y = predict(user_value)

    # Print the predicted y value for the input x
    print("Predicted y for", user_value, ":", predicted_y)

  except ValueError:
    # Handle invalid input (not an integer)
    print("Input must be an integer (e.g. 1, 2, 3, ...).")
