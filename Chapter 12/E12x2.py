# program E12x2.py
# reading from a file

def main():
    # open file for reading
        while True:
                try:
                    file_name=input('Enter filename for reading:\ ').strip()
                    infile= open(file_name, 'r')
                    break
                except IOError as ioe:
                    print ("Error: can\'t find file or read data")
                    print(ioe)
                    print(ioe.args)
                finally:
                        print('We have handled the exception')
        
    # reading
        print (infile.read())
        

main()
