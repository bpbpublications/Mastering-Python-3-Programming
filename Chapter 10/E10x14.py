# program E10x14.py
# reversing a string
def reverse(str1):
    length = len(str1)
    for i in range(length - 1, -1, -1):
        yield str1[i]

# For loop to reverse the string
for char in reverse('purposeful'):
                print(char)
