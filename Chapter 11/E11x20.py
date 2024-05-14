# you should execute the program in command prompt
# copy the path of the program file and execute as in book
# I had given
# C:\>"E:\Python final after copy editing\Python Program Files\E11x20.py" 100 200
# program E11x20.py
# command-line arguments
import sys	
	
def main():
    print('number of arguments=', len(sys.argv))
    print("argument 0 - file name is", sys.argv[0])
    print("argument 1 - ", sys.argv[1])
    print("argument 2 - ", sys.argv[2])
    
       
main()
