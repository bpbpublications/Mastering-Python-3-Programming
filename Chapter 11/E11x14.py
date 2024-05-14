# program E11x14.py
# writing and then reading a list using json
import json	
def main():
    # open file for writing and reading 
    with open("d2.txt", "w+") as iofile:
        list1=[2, 3, 7, 11, 13, 19, 23]
        json.dump(list1, iofile) # writing
        iofile.seek(0)
        list2=json.load(iofile)
        print(list2)

    iofile.close()
       
 
main()
