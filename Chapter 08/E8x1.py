'''Program E8x1.py'''
ELEMENTS=5 # A constant defined
tup1=65, 85, 105, 205, 15 # assignment without parentheses
print(tup1)
print(len(tup1))  # length of tup1 - should print 5
print (sum(tup1)) # should print 475
print('average= ', sum(tup1)/ELEMENTS) # should be 95
print (sorted(tup1))
print(tup1)# sorted cannot alter tup1
print (max(tup1))# should be 205
print (min(tup1))# should be 15

