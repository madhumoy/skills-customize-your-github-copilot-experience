# Import necessary libraries
import pandas as pd
import numpy as np

# Task 1: Load Data and Calculate Basic Statistics
# Load the CSV file
data = pd.read_csv('data.csv')

# Calculate mean, median, and standard deviation
mean_value = data['value'].mean()
median_value = data['value'].median()
std_value = data['value'].std()

# Print the results
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_value}")

# Task 2: Data Summary
# Generate summary statistics
summary = data.describe()
print("\nData Summary:")
print(summary)