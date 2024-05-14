# program E11x8.py
# copying from a source file to a destination file
import os.path
import sys	
	
def main():
    # open file for reading
    infile = open("d1.txt", "r")

 # open file for writing
   
    if os.path.isfile("e2.txt"):
        print('e2.txt exists')
        sys.exit()

    else:
        outfile=open("e2.txt", "w")
    # copying
        for line in infile:
            outfile.write(line)
    # checking contents of destination file
    outfile = open("e2.txt", "r")
    print(outfile.read())

    infile.close()
    outfile.close()
    
   
main()
