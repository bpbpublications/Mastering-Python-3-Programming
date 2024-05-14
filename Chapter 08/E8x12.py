'''Program E8x12.py'''
# Dictionary Methods 

def main():
    dct1={1:'Jan', 2:'Feb', 3:'March', 4:'April'}
    print(dct1) # keys and values of dictionary printed
    print(dct1.keys()) # keys will be printed as tuple
    print(dct1.values()) # values will be printed as tuple
    print(dct1.items())  # items printed as tuple
    print(dct1.get(3))    # will print march
    print(dct1.pop(3))  # march will be printed
    print(dct1.popitem()) # last item will be returned
    dct2={5:'May', 6:'June'} # new dictionary created
    dct1.update(dct2) # dct2 added to dct1
    print(dct1)

main()
