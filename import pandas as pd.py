import pandas as pd
import numpy as np

# Read the CSV data
df = pd.read_csv('data_pengangguran_up_to_2023.csv')

# Select the 'UnemploymentRate' column and convert it to a 2D numpy array
unemployment_rate = df['UnemploymentRate'].values.reshape(2, -1)

# Reverse the unemployment_rate array to read the data from the bottom up
reversed_array = np.flipud(unemployment_rate)

# Create an empty array with the same shape as reversed_array
filled_array = np.empty_like(reversed_array)

# Start filling the array from the bottom up and alternate between row one and two
row_one = 0
row_two = 1
for i in range(reversed_array.shape[1]):
    if i % 2 == 0:
        filled_array[row_one, i] = reversed_array[row_one, i]
        filled_array[row_two, i] = reversed_array[row_two, i]
    else:
        filled_array[row_one, i] = reversed_array[row_two, i]
        filled_array[row_two, i] = reversed_array[row_one, i]

print(filled_array)