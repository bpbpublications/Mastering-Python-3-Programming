# program E12x4.py
# divide 
	
def main():
    
        try:
            var1=eval(input('enter an integer: '))
            var2=eval(input('enter an integer: '))
            var3=var1/var2
            print('var3= ', var3)
        except ZeroDivisionError as er1:
            print('Divison by zero')
            print (er1.args)
            print(er1)
          
        except:
            print('unknown error')
        finally:
            print('program execution completed')
      
main()
