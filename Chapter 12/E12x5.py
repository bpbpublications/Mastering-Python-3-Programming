# give a message and also the quotient.
# program E12x5.py
# use of else
	
def main():
    
        try:
            var1=eval(input('enter an integer: '))
            var2=eval(input('enter an integer: '))
            var3=var1//var2
            
        except ZeroDivisionError as er1:
            print('Divison by zero')
            print (er1.args)
            print(er1)
          
        except:
            print('unknown error')

        else:
                print('no exception. result=', var1//var2)
      
main()
