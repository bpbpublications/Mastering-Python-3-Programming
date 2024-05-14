'''Program E7x7.py'''
# list comprehension
numbers=[1, 2, 3, 4, 5]
print(numbers)
numbers1=[num**2 for num in numbers if num%2==0] # square even 	# numbers
print(numbers1)
numbers2=[num**3 for num in numbers if num%2==1] # cube odd numbers
print(numbers2)
