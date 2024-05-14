# program E10x12.py
# Iterator
class Dec(object):
  def __iter__(self):
    self.num = 100
    return self

  def __next__(self):
    x = self.num
    if(x==0):
        raise StopIteration
    else:    
        self.num -= 2
        return x

even = Dec()
iter_even = iter(even)

print(next(iter_even))
print(next(iter_even))
print(next(iter_even))
