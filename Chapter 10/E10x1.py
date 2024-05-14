# program E10x1.py
# A Container class
class Bank:
    def get_bd(self):
               self._bankName='Bank of India'
               self._branch='Adayar'

    def display_bank(self):
        print('bank name =', self._bankName)
        print('branch name =', self._branch)
        
class Account:  # class definition
    def get_data(self, s, n, b):
        self.__acName=s
        self.__accountNum = n
        self.__balance =b
        self._obj=Bank()
        self._obj.get_bd()
        
    def display(self): 	# Method declaration
            print("Name =", self.__acName)
            print("Account number =", self.__accountNum)
            print("Balance        =", self.__balance)
            self._obj.display_bank()
	
def main():
    vinay = Account()   # creating object
    vinay.get_data('Ram', 1212, 10000.75)
    vinay.display() # calling a method

       
main()

