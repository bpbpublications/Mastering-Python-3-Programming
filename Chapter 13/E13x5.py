# Program E13x5.py
# perf_counter
from time import *
t1=perf_counter() # measure start time
sleep(16)
t2=perf_counter() # measure stop time
print('elapsed time =', t2-t1, 'seconds')
