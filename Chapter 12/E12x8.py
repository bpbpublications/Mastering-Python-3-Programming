class BalanceErrorException(RuntimeError):
    pass
class Account:  # class definition
    def get_data(self, s, n, b):
        self.__name=s
        self.__account = n
        self.__balance =b

    def debiting(self, amount):
        self.__balance-=amount
        if self.__balance < 10000:
            self.__balance+=amount
            raise BalanceErrorException
      
    def display(self): 	# Method declaration
            print("Name =", self.__name)
            print("Account number =", self.__account)
            print("Balance        =", self.__balance)
	
def main():
    Vinay = Account()   # creating object
    Vinay.get_data('Ram', 1212, 17000)
    Vinay.display() # calling a function
    while True:
        try:
            x=eval(input('Enter amount to be withdrawn: '))
            Vinay.debiting(x)
            break
        except:
            print('insufficient balance')
            print('withdrawal denied')
        finally:        
            Vinay.display()
main()

