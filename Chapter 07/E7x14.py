# program E7x14.py
# Circulate the values of n variables
def circulating(list1):
  
    for val in range (len(list1)):
        ele = list1.pop(0)
        list1.append(ele)
        print('circulated list is: ', list1)

def main():
    no_of_elements = int(input("Enter number of values : "))
    list0 = []
    val=0
    while val<no_of_elements:
        ele = int(input("Enter integer : "))
        list0.append(ele)
        val=val+1
    print('original sequence is ')
    print(list0)
    circulating(list0) # calling circulating

main()
