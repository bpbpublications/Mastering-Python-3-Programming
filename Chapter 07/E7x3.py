'''Program E7x3.py'''
list1=[111, 13, 123, 89, 71, 11, 89, 13]  # list created

print(list1)
list1.remove(13)  # Removes first occurrence of 13 in the list1
print(list1)
list1.pop(4)   # Removes element with index 4 from list1
print(list1)  #
list1.insert(2,33) # insert 33 at index 2
print (list1)
print(list1.count(89)) # counts the number of times 89 appears in list1
list2=[10, 20, 30]
list1.extend(list2) # appends list2 to list1
print(list1)
list1.reverse()
print(list1)
print(list1.index(111))
