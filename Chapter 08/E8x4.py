'''Program E8x4.py'''
#   Returning values as a tuple
import math
def rect(l, b):
    area=l*b
    perim=2*(l+b)
    diag=math.sqrt(l*l+b*b)
    return(area, perim, diag)

def main():
    l,b=eval(input('enter length and breadth of a rectangle:'))
    area, perimeter, diagonal=rect(l,b)
    print('area=', area)
    print('perimeter=', perimeter)
    print('diagonal=', diagonal)
      
main()
