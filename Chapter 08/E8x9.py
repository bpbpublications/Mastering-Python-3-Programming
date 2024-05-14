'''Program E8x9.py'''
# set operations 

marks1={100, 99, 98, 60, 10, 31, 17} 
marks2={77, 17, 100, 99, 98, 32, 17}
print("marks1: ", marks1)
print('marks2:' ,marks2)
print(marks1.union(marks2))  # elements in either list
print(marks1|marks2) # will get the same result
print(marks1.intersection(marks2)) # elements in both the lists
print(marks1&marks2)  # same result as above
print(marks1.difference(marks2)) # elements in marks1 and not in marks2
print(marks1-marks2)# same result as above
print(marks1.symmetric_difference(marks2))# elements in either set but not both
print(marks1^marks2) # exclusive or - same result as above
