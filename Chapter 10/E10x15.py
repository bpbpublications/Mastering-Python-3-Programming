# Example E10x15.py
# Generator expression within a for loop
numbers = [1, 2, 3, 4, 5]

# Using a generator expression to generate squares of numbers
squared_numbers = (x ** 2 for x in numbers)

# Iterating over the generator expression using a for loop
for squared_number in squared_numbers:
    print(squared_number)
