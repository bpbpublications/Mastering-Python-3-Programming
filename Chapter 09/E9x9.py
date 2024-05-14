# program E9x9.py
# docstring
class Account:
    ''' This is the definition of the class

    The class defines bank account'''
    def get_data(self, s, n, b):
        self.__name=s
        self.__account = n
        self.__balance =b
        
    def display(self):
        ''' this is a method to display object attributes'''
        print("Name =", self.__name)
        print("Account number =", self.__account)
        print("Balance        =", self.__balance)
	
def main():
    Vinay = Account()   # creating object
    Vinay.get_data('Ram', 1212, 10000.75)
    help(Account)
    help(Vinay.display())
    
main()
