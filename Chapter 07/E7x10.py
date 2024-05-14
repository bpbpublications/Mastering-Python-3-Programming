'''Program E7x10.py'''
# list cloning
list1=[1, 2, 3, 4, 5]
list2=list1[:] # slicing
del(list1[1])
print(list2)
list2.append(16)
print(list1)
print(list2)

