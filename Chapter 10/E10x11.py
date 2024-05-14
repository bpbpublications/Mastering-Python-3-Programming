# Program E10x11.py
# Abstract class
from abc import ABC, abstractmethod
class G_shape(ABC):
    @abstractmethod
     
    def perimeter(self):
        pass
class Square(G_shape):
    def perimeter(self):
        self._side=5
        return(4*self._side)

class Circle (G_shape):
    def perimeter(self):
        self._radius = 7
        return(2 * 3.14 * self._radius)
def calc_perimeter(input_obj):
    print(input_obj.perimeter())

      
def main():
    gs_obj=G_shape()
    calc_perimeter(gs_obj)
    s_obj=Square()
    calc_perimeter(s_obj)
    c_obj = Circle()
    calc_perimeter(c_obj)    
main()
