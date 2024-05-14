# program E11x11.py
# counting number of occurrences of each character in a text file
	
def main():
    filename=input('Enter file name:  type e2.txt   ')
    infile=open(filename, "r")
# print the contents of the file
    
    dict1=dict()

    for var in infile:
        print(var)
# Remove the leading spaces and new line characters
        var=var.strip()

        var=var.lower()

        for ch in var:
# Check if the character is already in dictionary
            if ch.isalpha():
                if ch in dict1:
                    dict1[ch]=dict1[ch]+1
                else:
# Add the character to dictionary with count=1
                    dict1[ch] =1
 
    for key in list(dict1.keys()): 
        print(key, ":", dict1[key])
  
      
main()
        
 
  
    
  

