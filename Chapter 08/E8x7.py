'''Program E8x7.py'''
# Built-in Functions on set
marks={100, 99, 98, 60, 10, 31, 17} 
print(marks)
print(len(marks)) # since length is 7 it will print 7
print(sum(marks))  # will print 415
print(min(marks)) # will print 10
print(max(marks)) # will print 100 
print(99 in marks)  # returns true
print(16 in marks)  # returns false
print(100 not in marks) # returns false
print(sorted(marks))
print(*marks) # unpacks the elements*
