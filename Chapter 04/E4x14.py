'''Program E4x14.py'''
# Conversion of strings to bytes
str1='God is Love'
print("The string for conversion : " + str(str1)) 
# Conversion  
byt1 = str1.encode('utf-8')
print('bytes=  ', byt1)
print("byte string: " + str(byt1))
print( "type : " + str(type(byt1)))
