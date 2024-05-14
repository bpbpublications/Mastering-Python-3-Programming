# Program E13x14.py
# Finding execution time with decorator
import time
def cpu_time(fun):
    def measure(*args, **kwargs):
        t1=time.perf_counter()
        result=fun(*args, **kwargs)
        t2=time.perf_counter()
        exec_time=t2-t1
        print('time taken by', fun.__name__, 'is ', exec_time, 'seconds')
        return result
    return measure

@cpu_time
# we had executed the program previously
# Finding square root of a number using math
def Sqrt1(x):
    import math
    return(math.sqrt(x))

@cpu_time
# we had executed the program previously
# Finding the square root of a number without using math function 
def Sqrt2(x):
    last_guess= x/2.0
    while True:
        guess= (last_guess + x/last_guess)/2
        if abs(guess - last_guess) < .000001: # example threshold
            return guess
        last_guess= guess

def main():
    x=eval(input('Enter a number to find square root: '))
    print('square root of ', x, 'is', Sqrt1(x))
    print('square root of ', x, 'is', Sqrt2(x))

     
main()
