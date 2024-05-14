# program E11x1.py
# writing to a file
import os.path
import sys	
def main():
    
        filename=input('Enter filename for writing - Type d1.txt  ')
        if os.path.isfile(filename):
            print('filename exists')
            sys.exit()
        else:
        # open file for writing
            outfile = open(filename, "w")
        # writing
            outfile.write('First line of Text\n')
            outfile.write('Second line of Text\n')
            outfile.write('Third Line of Text\n')
            outfile.close()
    
main()
