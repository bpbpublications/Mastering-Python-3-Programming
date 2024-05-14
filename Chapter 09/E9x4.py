# program E9x4.py
# A simple class
class Account:  # class definition
    def get_data(self, s, n, b):
        self.__name=s
        self.__account = n
        self.__balance =b

    def crediting(self, amount):
        self.__balance+=amount
        
    def display(self): 	# Method declaration
            print("Name =", self.__name)
            print("Account number =", self.__account)
            print("Balance        =", self.__balance)
	
def main():
    Vinay = Account()   # creating object
    Vinay.get_data('Ram', 1212, 10000.75)
    Vinay.display() # calling a function

    Vinay.crediting(12500)
    Vinay.display()

main()
