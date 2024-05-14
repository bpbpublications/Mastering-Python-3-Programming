# Program E7x12.py
# using Python arrays
from array import *
def main():
    a1=array('i',[12, 18, 6, 24, 72])# Integer array declared
    print('originl array is: ', a1)
    a3=a1*3 # repeat elements of array 3 times
    print('array repeated 3 times is: ', a3)
    print(type(a1)) # type of a1
    print(a1[2]) # print the array element with index 2
    for x in a1: # print all elements of array
        print(x)
    
main()
