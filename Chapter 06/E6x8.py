# Program E6x8.py
# Finding power

def power (x, y):
    if y==0:
        return 1
    elif y==1:
        return x
    else:
        return pow(x,y)

def main():
    x1=int(input("enter x1 : "))
    y1=int(input("enter y1 : "))
    print(power(x1, y1))

main()
