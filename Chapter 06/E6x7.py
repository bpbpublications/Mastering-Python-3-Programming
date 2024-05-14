# Program E6x7.py
# Finding the square root of a number without using math function 
def Sqrt(x):
    last_guess= x/2.0
    while True:
        guess= (last_guess + x/last_guess)/2
        if abs(guess - last_guess) < .000001: # example threshold
            return guess
        last_guess= guess

def main():
    x=eval(input('Enter number whose square root is needed :'))
    print(Sqrt(x))
    
main()
