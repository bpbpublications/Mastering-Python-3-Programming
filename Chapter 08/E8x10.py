'''Program E8x10.py'''
# set operations 

set1={100, 99, 98, 60, 10, 31, 17} 
set2={100, 60, 31, 17}
print(set1.issuperset(set2)) # should be True
print(set1.issubset(set2)) # should be False
print(set1==set2) # should be False
