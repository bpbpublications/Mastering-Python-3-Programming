'''Program E8x3.py'''
# additional operations on lists

tup1=15, 65, 85, 105, 205 # create a tuple
tup2=('Oh', 'my', 'God')
tup3=(tup1, tup2) # creating tuple of tuples
print('tup3= ', tup3)
tup4=(11, 22, tup2, 33) # embedding tup2 in tup4
print(tup4)
tup5=('me', 'you', *tup2, 'thank you') # unpacking tup2 
print(tup5)
