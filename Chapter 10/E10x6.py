# program E10x6.py
# base class
class Book(object):
    def __init__(self, t, au):
        self._title = t
        self._author = au


    def display(self):
        print('Title: ', self._title)
        print('Author: ', self._author)
        print(self)
        
def main():
    obj1 = Book('TQM',"Subburaj Ramasamy")
    obj1.display()
main()
