# program E12x3.py
# word count in a text file
	
def main():
    while True:
        try:
            filename=input('Enter file name: ').strip()
            infile=open(filename, "r")
            break
        except IOError:
            print(filename, ' does not exist')
        
    dict1=dict()   # Empty dictionary
    for line in infile:
        line=line.strip()
        line=line.lower()
        words=line.split(" ")
        for word in words:
            if word in dict1:
                dict1[word]=dict1[word]+1
            else:
                dict1[word] =1
    for key in list(dict1.keys()): 
        print(key, ":", dict1[key])
  
main()

        
 
  
    
  

