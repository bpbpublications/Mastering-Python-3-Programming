# program E11x16.py
# writing and then reading a dictionary using json
import json	
def main():
    # open file for writing and reading 
    with open("d2.txt", "w+") as iofile:
        dct3={'Jan':1, 'Feb':2, 'March':3, 'April':4}
        json.dump(dct3, iofile) # writing
        iofile.seek(0)
        dct3=json.load(iofile)
    print(dct3)
    iofile.close()
       
   
main()
