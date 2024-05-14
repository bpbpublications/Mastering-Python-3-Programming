# program E13x12.py
# Decorator Function
def decor(fun):
    def wrap():
        print("====================")
        fun()
        print("////////////////////")
    return wrap

def sayhi():
          print("Hi Friend")
newfunc=decor(sayhi)
newfunc()
