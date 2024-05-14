'''Program E6x14.py'''
# variable length arguments
# called function 
def called(*args): # function header
    for var in args:
        print(var)
    print("\nData type of argument:",type(args))   

# calling function
def main():
    called(9)
    called(23, 65)
    called(2,3,4)
    called(45, 67.8, 'subhash')
main() # main function call
