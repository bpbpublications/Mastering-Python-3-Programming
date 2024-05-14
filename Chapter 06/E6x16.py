'''Program E6x4.py'''
# Finding Greatest Common Divisor of 2 given numbers
# called function 
def gcd(num1, num2): # function header
    if(num2==0):
        return num1
    else:
         return(gcd(num2, num1%num2))
 

# calling function
def main():
    a=eval(input('enter an integer: '))
    b=eval(input('enter an integer: '))
    if b>a:    # swap the numbers
        temp=a
        a=b
        b=temp
    result = gcd(a,b)
    print('gcd of', a,'and', b,'= ', result)

main() # main function call
