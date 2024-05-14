'''Program E8x11.py'''
# Dictionary operations 

dct1={1:'Jan', 2:'Feb', 3:'March', 4:'April'}
dct1[5]='May'
print(dct1) # May will be added
dct1[1]='January' # modifying Jan to January
print(6 in dct1) # checks presence of 6 in dct1
print(6 not in dct1) # Checks absence of 6 in dct1
print(len(dct1))  # prints the number of elements
print(max(dct1)) # prints maximum key value
print(min(dct1)) # prints minimum key value
print(list(dct1)) # prints keys as a list in order of insertion
print(sorted(dct1)) # prints sorted keys as a list
del(dct1[3]) # it will delete key value pair with key =3
print(dct1)
del(dct1) # the object will be deleted and no elements left
print(dct1)
