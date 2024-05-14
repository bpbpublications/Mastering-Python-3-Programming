# program E7x15.py
# Linear Search
def read_key():
    key_item = eval(input("Enter the key item to search: "))
    return key_item

def linear_search(search_key):
    ia = [10, 20, 30, 40,50]
    found = False
    n=len(ia)
    i=0
    while (i<n-1) & (found==False):
        if ia[i] == search_key:
             found = True
             break
        else:
            i+=1
    if found:
        print('Item found at location',  i + 1)
    else:
        print("Item not found in the list")
def main():
    key = read_key()
    linear_search(key)

main()
