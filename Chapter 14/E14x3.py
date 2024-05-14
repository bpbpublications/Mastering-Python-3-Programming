# Program E14x3
#  simulates que using deque

from collections import deque
   
que = deque() # Empty deque 
  
# add using append()method deque 
 
que.append(10)
print('\nQueue now contains:', que)
que.append(20)
print('\nQueue now contains:', que)
que.append(30)
print('\nQueue now contains:', que)
que.append(35)
print('\nQueue now contains:', que)

 
# remove from que   

print('removed :', que.popleft())
print('\nQueue now contains:', que)
print('removed :', que.popleft())
print('\nQueue now contains:', que)
print('removed :', que.popleft())
print('\nQueue now contains:', que)


