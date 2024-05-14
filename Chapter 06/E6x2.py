'''Program E6x2.py'''
# called function 
def sum(num1, num2): # function header
    total=num1+num2
    return total


# calling function
def main():
    a=eval(input('enter a number: '))
    b=eval(input('enter a number: '))
    sum1=sum(a,b)
    print('sum of the numbers a and b=', sum1)
    c=eval(input('enter a number: '))
    d=eval(input('enter a number: '))
    sum2=sum(c,d)
    print('sum of the numbers c and d=', sum2)
    print('sum of sum1 and sum2', sum(sum1,sum2))

if __name__=='__main__':
    main() # main function call
