# Salary Data Analysis and Prediction

This project analyzes and visualizes salary data, including calculations of statistical measures and predictions based on years of experience. The program uses Python with libraries such as `pandas`, `numpy`, `matplotlib`, and `scikit-learn`.
# Description
- Data Loading: Loads data from Salaryydata.xlsx using pandas.
- Frequency Table Creation:Bins the salary data into 5 equal ranges.
- Creates a frequency table and displays the counts within each salary range.
- Histogram: Plots a histogram showing the distribution of salary data.
- Ogive (Cumulative Frequency Curve): Plots the cumulative frequency of salaries.
- Statistical Measures: Calculates the mean, median, and mode for the salary data.
- Computes the quartile deviation (measure of spread) and standard deviation.
- Scatter Plot: Visualizes the relationship between salary and years of experience.
- Correlation Coefficient: Computes the correlation between salary and years of experience.
- Linear Regression Model:Fits a linear regression model to predict salary based on years of experience.
- Displays the regression equation.
- Prediction: Predicts the salary for a specified number of years of experience (e.g., 12 years).
## Requirements

To run this program, you need:

- Python 3.7 or above
- Required libraries: `pandas`, `numpy`, `matplotlib`, `scikit-learn`
- An Excel file named `Salaryydata.xlsx` containing the columns:
  - `Salary`: Salary of employees
  - `YearsExperience`: Years of experience of employees

Install the required packages using:

```bash
pip install pandas numpy matplotlib scikit-learn
