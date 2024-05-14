# Program E11x19.py
# Reading CSV files
import csv

# Open the CSV file
with open('data.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Each row is a list of values separated by commas
        print(row)

