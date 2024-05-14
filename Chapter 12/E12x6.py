# program E12x6.py
# ValueError
def main():
    
        try:
            var1=int(input('enter an integer: '))
            var2=int(input('enter an integer: '))
            var3=var1//var2
            
        except ZeroDivisionError as er1:
            print('Divison by zero')
            print (er1.args)
            print(er1)

        except ValueError as ive:
                print('ValueError Exception')
                print(ive)
                print(ive.args)
        else:
                print('no exception. result=', var1//var2)
      
main()
