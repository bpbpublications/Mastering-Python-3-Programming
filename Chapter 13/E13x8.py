# Program E13x8.py
# process_time for finding CPU time
from time import *
t1=process_time() # measure start time
squares=[]
for num in range(100000):
	squares.append(num*num)
sleep(5)
t2=process_time() # measure stop time
print('elapsed time =', t2-t1, 'seconds')
