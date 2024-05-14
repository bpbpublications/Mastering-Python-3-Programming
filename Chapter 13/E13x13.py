# program E13x13.py
# Decorator Function with arguments

def decor1(fun):
        def wrap(*args,**kwargs):
            if args[1]==0:
                 print('second argument is zero')
                 return
            return fun(*args,**kwargs)
        return wrap
@decor1
def div1(a,b):
    print(a/b)
@decor1
def subtn(a,b):
    print(a-b)

div1=decor1(div1)
subtn=decor1(subtn)

x,y=eval(input('Enter two numbers - separated by comma: '))
div1(x,y)
subtn(x,y)

