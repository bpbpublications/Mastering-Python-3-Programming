# Program E10x10.py
# Dynamic Binding

class G_shape(object):
           
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
      
def main():
    g_obj=G_shape()
    def display(g_obj):
        print(g_obj.__str__())
    display(g_obj)
    s_obj=Square()
    display(s_obj)
    display(s_obj.perimeter())
    c_obj = Circle()
    display(c_obj)
    display(c_obj.perimeter())
    
main()
