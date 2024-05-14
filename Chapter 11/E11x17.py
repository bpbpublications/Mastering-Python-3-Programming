# program E11x17.py
# writing into string and then reading from it using json
import json	
def main():
        list1=[2, 3,5, 7, 11, 13, 17]
        tup2=('mohan', True, 11, 4.8)
        dct3={'Jan':1, 'Feb':2, 'March':3, 'April':4}
        str1=json.dumps(list1)# writing list1 to str1
        str2=json.dumps(tup2) # writing tup2 to str2
        str3=json.dumps(dct3) # writing dct3 to str3

        i=json.loads(str1)
        j=tuple(json.loads(str2))
        k=json.loads(str3)
        print('list1=', i)
        print('tup2=', j)
        print('dct3=', k)
           
   
main()
