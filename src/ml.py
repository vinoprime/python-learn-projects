print("Hello ml")
# 1. import the data
# 2. clean the data
# 3. Split the data (Traning Set 80% of data / Test Set 20% of data)
# 4. Create a Model
# 5. Check the output
# 6. Improve





#  We'll create a basic model to predict student scores based on the number of hours they study.


import numpy as np
import matplotlib.pyplot as plt

# Sample data: Number of hours studied and corresponding exam scores
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
exam_scores = np.array([25, 45, 60, 70, 80, 85, 88, 92, 95, 97])

# Calculate the mean of hours studied and exam scores
mean_hours = np.mean(hours_studied)
mean_scores = np.mean(exam_scores)

# Calculate the slope (theta1) and y-intercept (theta0) of the regression line
# formula y = sumation of i=1 to n (xi-x^)(yi-y^)/ sumation of i=1 to n (xi-x^)^2
numerator = np.sum((hours_studied - mean_hours) * (exam_scores - mean_scores))
denominator = np.sum((hours_studied - mean_hours) ** 2)
theta1 = numerator / denominator
theta0 = mean_scores - theta1 * mean_hours

# Create the regression line
regression_line = theta0 + theta1 * hours_studied

print(theta0,theta1,hours_studied)
mean_hours


# Plot the data points
plt.scatter(hours_studied, exam_scores, label='Actual Scores')

# Plot the regression line
plt.plot(hours_studied, regression_line, color='red', label='Regression Line')

# Customize the plot
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.title('Linear Regression in Education')
plt.legend()
plt.grid()

# Show the plot
plt.show()
