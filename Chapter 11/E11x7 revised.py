# revised program E11x7.py
# implicit method for reading
	
def main():
    # open file for reading
    with open("e2.txt", "r") as infile:
    # reading
        for line in infile:
            print (line)
       
main()
