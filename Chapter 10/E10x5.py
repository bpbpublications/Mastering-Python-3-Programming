# program E10x5.py
# Multiple Inheritance
# base class 1
class Book:
    def __init__(self, bookTitle, auth):
        self._title = bookTitle
        self._author = auth
class Agency:   #base class 2
    def __init__(self, namAgency, loc):
        self._name=namAgency
        self._location=loc
        
class Price(Book, Agency):
    def __init__(self, title, author,name, location, price):
        Book.__init__(self,title, author)
        Agency .__init__(self, name, location)
        self._price = price


    def display(self):
        print('Title: ', self._title)
        print('Author: ', self._author)
        print('Publisher:', self._name)
        print('location:', self._location)
        print('Price: ', self._price)
      
         
def main():
    obj3 = Price('Python',"Subburaj Ramasamy", "BPB" , "New Delhi", "550")
    obj3.display()
main()
