# program E9x3.py
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
    print('id of Vinay object=', id(Vinay))
    print(type(Vinay))
    Vinay.display() # calling a function

    # creating second object
    Karthik = Account()   # creating object
    Karthik.get_data('Sita', 1213, 24578.90)
    print('id of Karthik object=', id(Karthik))
    print(type(Karthik))
    Karthik.display() # calling a function

    # creating third object
    m= Account()   # creating object
    m.get_data('mary', 1214, 20000)
    print('id of m object=', id(m))
    print(type(m))
    m.display() # calling a function

main()
