# Program E13x7.py
# perf_counter to find CPU time
from time import *
t1=perf_counter() # measure start time
squares=[]
for num in range(100000):
	squares.append(num*num)
sleep(5)
t2=perf_counter() # measure stop time
print('elapsed time =', t2-t1, 'seconds')
