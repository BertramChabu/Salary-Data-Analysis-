from statistics import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_excel("Salaryydata.xlsx")
salary_data = data['Salary']

# Create frequency bins for grouped frequency table
num_bins = 5
bin_edges = np.linspace(salary_data.min(), salary_data.max(), num_bins + 1)
frequency_table = pd.cut(salary_data, bins=bin_edges, include_lowest=True).value_counts().sort_index()

# Display the frequency table
frequency_table_df = pd.DataFrame({'Salary Range': frequency_table.index.astype(str), 'Frequency': frequency_table.values})
print(frequency_table_df)

# Histogram
plt.hist(salary_data, bins=bin_edges, edgecolor='black', alpha=0.7)
plt.title("Histogram of Salaries")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Ogive
cumulative_frequency = np.cumsum(frequency_table.values)
plt.plot(bin_edges[1:], cumulative_frequency, marker='o', linestyle='-', color='b')
plt.title("Ogive of Salaries")
plt.xlabel("Salary")
plt.ylabel("Cumulative Frequency")
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.show()

# Calculate the mean, median, and mode for Salary
mean_salary = salary_data.mean()
median_salary = salary_data.median()
mode_salary = salary_data.mode().iloc[0]  # In case there are multiple modes

print(f"Mean Salary: {mean_salary}")
print(f"Median Salary: {median_salary}")
print(f"Mode Salary: {mode_salary}")

# Quartile deviation
q1 = salary_data.quantile(0.25)
q3 = salary_data.quantile(0.75)
quartile_deviation = (q3 - q1) / 2

# Standard deviation
std_dev_salary = salary_data.std()

print(f"Quartile Deviation: {quartile_deviation}")
print(f"Standard Deviation: {std_dev_salary}")

# Scatter plot for Salary vs. Years of Experience
plt.scatter(data['YearsExperience'], salary_data, color='blue')
plt.title("Scatter Plot of Salary vs Years of Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# Calculate correlation coefficient
correlation = data['YearsExperience'].corr(salary_data)
print(f"Correlation Coefficient: {correlation}")



# Reshape data for sklearn
X = data['YearsExperience'].values.reshape(-1, 1)
y = salary_data.values

# Fit the model
regression_model = LinearRegression()
regression_model.fit(X, y)

# Regression coefficients
slope = regression_model.coef_[0]
intercept = regression_model.intercept_
print(f"Regression Equation: Salary = {intercept} + {slope} * YearsExperience")

# Predict salary for 12 years of experience
predicted_salary = regression_model.predict([[12]])
print(f"Estimated Salary for 12 years of experience: {predicted_salary[0]}")
