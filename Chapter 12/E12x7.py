# Progran E12x7
# using raise for exception
try:
    x=int(input('enter an integer: '))
    if x<0:
        raise Exception("negative number")
    elif not type(x) is int:
        raise ValueError("Only integers are allowed")
except ValueError as er1:
        print('invalid type')
        print (er1.args)
        print(er1)
          
except:
        print('unknown error')
