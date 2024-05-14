'''Program E8x8.py'''
# Methods of class set

marks={100, 99, 98, 60, 10, 31, 17} 
s1={'Joseph', 'Peter', 'Thomas'}
marks.update(s1) #adds s1 to marks
print(marks)
s1.add('Xavier') # adds Xavier to s1
print(s1)
marks.remove(100) # deletes 100 from marks
print(marks)
s1.clear() # Removes all elements from s1
print(s1)
