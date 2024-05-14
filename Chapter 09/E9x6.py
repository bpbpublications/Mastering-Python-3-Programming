# program E9x3.py
# operator overloading
class Complex:  # class definition
    def __init__(self, r=0, i=0.0):
            self. __real = r
            self. __imag =i

    def __sub__(self,other):
        comp1=Complex()
        comp1.real = self.__real - other.__real
        comp1.imag = self.__imag - other.__imag
        return comp1
    
    def display(self): 	# Method declaration
        print("difference =", self.real, self.imag, 'j' )
            

    def __del__(self):
        print('object deleted: '+str(self))
    
def main():
    num1 = Complex(8,7)   # creating object
    num2 = Complex(3,4)
    num3=num1-num2
    num3.display() # calling a function

    num1 = Complex(200.75,27.75)   # creating object
    num2 = Complex(100.25,100.5)
    num3=num1-num2
    num3.display() # calling a function 

main()

