# Program E6x5.py
# Finding distance between two points

def dist(x1, y1, x2, y2):
    result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
    print("distance between",(x1,y1),"and",(x2,y2),"is : ",result)

def main():
    x1=int(input("enter x1 : "))
    y1=int(input("enter y1 : "))
    x2=int(input("enter x2 : "))
    y2=int(input("enter y2 : "))
    dist(x1, y1, x2, y2)

main()
