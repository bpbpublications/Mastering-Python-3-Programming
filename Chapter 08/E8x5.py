'''Program E8x5.py'''
#   Returning values as a list
import math
def sqre(l):
    area=l*l
    perim=4*l
    diag=math.sqrt(2)*l
    return[area, perim, diag]

def main():
    length=eval(input('enter length of a square:'))
    area, perimeter, diagonal=sqre(length)
    print('area=', area)
    print('perimeter=', perimeter)
    print('diagonal=', diagonal)
      
main()
