#  Program E14x5.py
# Bubble sort
def bubble(array):
    print("list to be sorted is: ", array)
    for i in range(4):
            for j in range(i+1, 5):
                if(array[i] > array[j]): 
                        temp=array[i]
                        array[i]=array[j]
                        array[j]=temp
            print("after pass", i+1, ":",  array)
    return array

def main():
    arr=[89, 12, 75, 34, 2]
    arr1=bubble(arr)
    print('sorted list is:', arr1)

main()
