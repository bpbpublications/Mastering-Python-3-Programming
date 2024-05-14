'''Program E8x2.py'''
# Some more Operations using built in Functions

tup1=15, 65, 85, 105, 205 # create a tuple
tup2=('Oh', 'my', 'God')
print('concatenation ', tup1+tup2)
print('duplicate ', 2*tup2)
print('slicing ', tup1[1:3])
print(205 in tup1) # in operator- should get true
for var in tup2:   # printing elements in a tup1
    print(var, end='\n')
print(tup1==tup2) # result should be false
