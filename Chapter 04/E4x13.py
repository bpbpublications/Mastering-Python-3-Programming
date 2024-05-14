'''Program E4x13.py'''
# Conversion of strings to bytes
str1='God is Love'
print("The string for conversion : " + str(str1)) 
# Conversion  
byt1 = bytes(str1, 'utf-8') # converts str1 to bytes in UTF-8 format
print('bytes=  ', byt1)
print("bytes string: " + str(byt1))
print("type : " + str(type(byt1)))
