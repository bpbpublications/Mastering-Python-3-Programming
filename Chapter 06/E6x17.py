# Program E6x17.py
# Finding exponentiation of a number

def expo(base,pow):
    if(pow==1):
        return(base)
    elif(pow!=1):
        return(base*expo(base,pow-1))

def main():
    x=eval(input("Enter base: "))
    y=int(input("Enter integer for exponential value: ")) 
    print(expo(x,y))
    
main()    

