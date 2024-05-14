# Program E6x10.py
# Boolean Function 


def is_evenly_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

def main():
    x=int(input("Enter an integer:"))
    y=int(input("Enter an integer:"))
    z=is_evenly_divisible(x,y)
    if z==True: 
        print(x,'is evenly divisible by ', y)
    else:
        print(x,'is NOT evenly divisible by ', y)

main()
