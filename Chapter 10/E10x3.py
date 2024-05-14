# program E10x3.py
# Single Inheritance

class Youth:
    
    def __init__(self, first, last):
        self._first_name = first
        self._last_name = last

    def display(self):
            print('first_name:', self._first_name)
            print('last name: ', self._last_name)
        
class Student(Youth):

        def __init__(self, first, last, roll_num):
            Youth.__init__(self, first, last)
            self.__roll_num=roll_num

        def display(self):
                print('first_name:', self._first_name)
                print('last name: ', self._last_name)
                print('roll_num:', self.__roll_num)
        
def main():

        per1=Youth("manoj", "prabhakar")
        per2=Student("manoj", "prabhakar", "IT802")

        per1.display()
        per2.display()

main()
