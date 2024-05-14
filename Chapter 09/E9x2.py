# program E9x2A.py
# A complete class
class Account:  # class definition
    def __init__(self, s ='', n=0, b=0.0):
        self.__name=s
        self.__account = n
        self.__balance =b

    def get_data(self, s, n, b):
        self.__name=s
        self.__account = n
        self.__balance =b
        
    def display(self): 	# Method declaration
            print("Name =", self.__name)
            print("Account number =", self.__account)
            print("Balance        =", self.__balance)

    def __del__(self):
            print('object deleted: '+str(self))
    
def main():
    Vinay = Account()   # creating object
    Vinay.get_data('Ram', 1212, 10000.75)
    Vinay.display() # calling a function

    # creating second object
    Karthik = Account()   # creating object
    Karthik.get_data('Sita', 1213, 24578.90)
    Karthik.display() # calling a function

    # creating third object
    m= Account()   # creating object
    m.get_data('mary', 1214, 20000)
    m.display() # calling a function

main()

