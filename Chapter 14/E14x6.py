# Program E14x3.py
# Selection sort

def selection_sort(arr):
    print('unsorted list:', arr)
    # i indicates number of items to be sorted
    for i in range(len(arr)):
        '''To find the minimum value of the unsorted segment,
         We first assume that the first element is the lowest'''
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(arr)):
            # Update the min_index if the element at j is lower than it
            if arr[j] < arr[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print('after pass=', i+1, arr)
    return(arr)

def main():
    list1=[33, 42, 5,3, 6, 22, 1]
    list2=selection_sort(list1)
    print('sorted list is: ', list2)
        

main()
