# execute the program in command prompt as given in the book
# I copied the path of the program, source file and destination file and executed

# program E11x21.py
# file copy
import sys, getopt
import shutil
	
def main():
    source=sys.argv[1]
    dest=sys.argv[2]
    shutil.copyfile(source, dest)
    outfile=open(dest, 'r')
    print(outfile.read())

main()
