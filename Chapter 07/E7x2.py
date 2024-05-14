'''Program E7x2.py'''
ELEMENTS=6 # A constant defined
list1=[]  # Empty list created
for i in range(ELEMENTS): # for loop will run 6 times
    data=eval(input('Enter a new integer: '))
    list1.append(data)
print(list1)
print(len(list1))  # function len finds length of list1-will print 6
print (sum(list1)) # finds sum of all elements of list1
print (sorted(list1))# sort the elements in list1
print (max(list1)) # Find maximum in the list1
print (min(list1))  # Find the minimum in the list1
