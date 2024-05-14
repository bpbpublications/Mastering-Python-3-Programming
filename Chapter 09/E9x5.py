# program E9x5.py
# To demonstrate class variables
class Account:  # class definition
    No_of_Accounts=0  # class data member
    
    def __init__(self, s ='', n=0, b=0.0):
        self.__name=s
        self.__account = n
        self.__balance =b
        Account.No_of_Accounts+=1
       

    def get_data(self, s, n, b):
        self.__name=s
        self.__account = n
        self.__balance =b
        
        
    def display(): 	# class method
            print('Number of Accounts=', Account.No_of_Accounts)
           

    def __del__(self):
            print('object deleted: '+str(self))
    
def main():
    Vinay = Account()   # creating object
    Vinay.get_data('Ram', 1212, 10000.75)
    Account.display() # class calling its method
    # creating second object
    Karthik = Account()   # creating object
    Karthik.get_data('Sita', 1213, 24578.90)
    Account.display()

    # creating third object
    m= Account()   # creating object
    m.get_data('mary', 1214, 20000)
    Account.display() 
    

main()
