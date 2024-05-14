# program E10x4.py
# Multi-level Inheritance
# base class
class Book:
    def __init__(self, bookTitle, auth):
        self._title = bookTitle
        self._author = auth

class Price(Book):
    def __init__(self, title, author, price):
        Book.__init__(self,title, author)
        self._price = price

class Agency(Price):
    def __init__(self, title, author, price, publisher):
        Book.__init__(self, title, author)
        Price.__init__(self, title, author, price)
        self._publisher=publisher
    def display(self):
        print('Title: ', self._title)
        print('Author: ', self._author)
        print('Price: ', self._price)
        print('publisher:', self._publisher)
         
def main():
    obj3 = Agency('Python',"Subburaj Ramasamy", "550","BPB" )
    obj3.display()
main()
