# program E11x15.py
# writing and then reading a tuple using json
import json	
def main():
    # open file for writing and reading 
    with open("d2.txt", "w+") as iofile:
        tup1=('Ram',189923, 4000.55)
        json.dump(tup1, iofile) # writing
        iofile.seek(0)
        tup2=json.load(iofile)
    print(tup2)
    iofile.close()
       
   
main()
