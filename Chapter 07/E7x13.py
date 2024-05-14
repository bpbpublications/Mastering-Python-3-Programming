# Program E7x13
# sum an array of numbers
from array import *
def main():
    a1=array('i',[12, 18, 6, 24, 72])# Integer array declared
    print('original array is: ', a1)
    sum=0
    for x in a1:
        sum=sum+x
    print('sum=', sum)
     
main()
