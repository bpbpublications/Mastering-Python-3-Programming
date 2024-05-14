# Program E7x17.py
# binary search
def read_key():
    key_item = eval(input("Enter the key item to search: "))
    return key_item
  
def binary_search(search_key):
    a=[2, 3, 5, 7, 11, 13]
    n=len(a)
    left = 0
    right = n-1
    found = False 
    while (left <=right)& (found==False):
        mid = (left + right)//2
        if a[mid] ==search_key:
                    found =True
        elif (a[mid] < search_key):
                    left = mid + 1 
        else:
                    right = (mid-1)
    if found==True:
        print('Item found at location',  mid+1)
    else:
        print("Item not found in the list")
def main():
    key = read_key()
    binary_search(key)

main()
