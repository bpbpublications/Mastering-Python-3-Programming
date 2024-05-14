# Program E6x3.py
# called function reverse 

def reverse(number): # function header
    rev=0
    while(number > 0):
        rev = rev * 10 +  (number % 10 )
        number = number//10
    return rev

# called function multiply
def multiply(number):
    print('double of the number=', 2*number)

# called function addDigits
def addDigits(number):
    sum = 0
    while number > 0:
            sum = sum + (number % 10)
            number = number // 10
    return (sum)
 
# calling function
def main():
    num=eval(input('enter a number: '))
    if num%2==1:
        print('reverse of the typed number=', reverse(num))
    else:
        multiply(num)
    if num%3==0:
        print('sum of digits=', addDigits(num))
           

main() # main function call

