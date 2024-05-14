# program E7x16.py
def read_key():
    key_item = eval(input("Enter the key item to search:within quote "))
    return key_item

def linear_search(search_key):
    ia = ['ram', 'krishna', 'sita', 'mary','vidhya']
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
