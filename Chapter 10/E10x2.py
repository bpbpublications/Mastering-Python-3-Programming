# program E10x2.py
# A Container class creating 3 objects
class Bank:
    def get_bd(self):
               self._n='Bank of India'
               self._b='Adayar'

    def display_bank(self):
        print('bank name =', self._n)
        print('branch name =', self._b)
        
class Account:  # class definition
    def get_data(self, s, n, b):
        self.__name=s
        self.__account = n
        self.__balance =b
        self._obj=Bank()
        self._obj.get_bd()
        
    def display(self): 	# Method declaration
            print("Name =", self.__name)
            print("Account number =", self.__account)
            print("Balance        =", self.__balance)
            self._obj.display_bank()
	
def main():
    vinay = Account()   # creating object
    vinay.get_data('Ram', 1212, 10000.75)
    vinay.display() # calling a function

    joseph = Account()
    joseph.get_data('Joseph', 1213, 20000.50)
    joseph.display()

    sridhar=Account()
    sridhar.get_data('Sridhar', 1214, 15000.25)
    sridhar.display()

    
main()

