# Program E6x9.py
# Finding area of triangle
import math
def area(a, b, c):
    s=half_perim(a,b,c)
    area1 = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area1
    
        
def half_perim(x,y, z):
        return (x+y+z)/2
    
def main():
    x1=int(input("enter x1 : "))
    y1=int(input("enter y1 : "))
    z1=int(input("enter x1 : "))
    print(area(x1, y1, z1))

main()
