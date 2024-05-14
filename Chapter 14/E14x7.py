# Program E14x7.py
# Insertion sort

def insertion_sort(arr):
    print('list to be sorted=', arr)
    for i in range (1,len(arr)):
            temp=arr[i]
            j=i-1
            while (temp<arr[j] and j>=0):
                arr[j+1]= arr[j]
                j=j-1
            arr[j+1] =temp
            print('list after', i, ' pass', arr)
        
    return(arr)
        

def main():
    list1=[33, 42, 5,3, 6, 22, 1]
    list2=insertion_sort(list1)
    print('sorted list is: ', list2)
        

main()
