# program E11x10.py
# counting number of occurrences of each word in a text file
	
def main():
    filename=input('Enter file name:       type e2.txt    ').strip()
    infile=open(filename, "r")   
        
    dict1=dict()

    for line in infile:
# Remove the leading spaces and new line characters
        line=line.strip()

        line=line.lower()
# split the line into words
        words=line.split(" ")

        for word in words:
# Check if the word is already in dictionary
            if word in dict1:
                dict1[word]=dict1[word]+1
            else:
# Add the word to dictionary with count=1
                dict1[word] =1
 
    for key in list(dict1.keys()): 
        print(key, ":", dict1[key])
  
      
main()
        
 
  
    
  

