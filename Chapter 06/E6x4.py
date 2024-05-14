# program E6x4.py
# Exchange the Value of 2 variables

def swap(var1, var2):
    print('original value of var1=', var1, 'var2=', var2) 
    temp=var1
    var1=var2
    var2=temp
    print('new value of var1=', var1, 'var2=', var2)

def main():
    x=input('Enter a variable:')
    y=input('Enter a variable:')
    swap(x, y) # calling swap function
main()
