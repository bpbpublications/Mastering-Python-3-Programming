# program E12x11.py
# Custom Exception

class TriangleInequalityException(RuntimeError):
    def __init__(self,s1, s2, s3):
        self.side1=s1
        self.side2=s2
        self.side3=s3
class Triangle:  # class definition
    def get_data(self, s1, s2, s3):
        self.side1=s1
        self.side2=s2
        self.side3=s3
        
    def perim(self):
        if self.side1 + self.side2 < self.side3 or\
           self.side2 + self.side3 < self.side1 or\
           self.side1 + self.side3 < self.side2:
             raise TriangleInequalityException(self.side1,self.side2,self.side3)
        else:
            return (self.side1 +self.side2+self.side3)
def main():
    tgle=Triangle()
    while True:
        try:
            x, y, z=eval(input("Enter the 3 sides of the triangle - separated by commas :"))
            tgle.get_data(x,y,z)
            print('perimeter= ', tgle.perim())
            break
        except TriangleInequalityException as tie:
            print('sides', tgle.side1, tgle.side2, tgle.side3, 'cannot form a triangle')
            print(tie.args)
            
main()

