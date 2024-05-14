'''Program E6x1.py'''
# called function 
def sum(num1, num2): # function header
    total=num1+num2
    return total


# calling function
def main():
    a=eval(input('enter an integer: '))
    b=eval(input('enter an integer: '))
    print('sum of the numbers=', sum(a,b))
    print(__name__)

main() # main function call
