# Program E6x11.py
# global and local scope 
x = 5
# Uses global because there is no local 'x' 
def fun1(): 
    print('Inside fun1() : ', x)
# Variable 'x' is redefined as a local 
def fun2():     
    x = 7
    print( 'Inside fun2() : ',x) 
# Uses global keyword to modify global 'x' 
def fun3():     
    global x 
    x = 9
    print('Inside fun3() : ',x)
def main():
    print ('global : ',x) 
    fun1() 
    print ('global : ',x) 
    fun2() 
    print ('global : ',x) 
    fun3() 
    print ('global : ',x) 

main()
