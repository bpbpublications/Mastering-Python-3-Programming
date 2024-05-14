'''Program E8x13.py'''
# Dictionary comprehension 

def main():
    dct1={1:'Jan', 2:'Feb', 3:'March', 4:'April'}
    print(dct1) # keys and values of dictionary printed
    print(dct1.keys()) # keys will be printed as tuple
    dct2={key**4:value for (key, value) in dct1.items()}
# dct2 with new values which are old value^4 will be created
    print(dct2)

    dct3={'Monday':1, 'Tuesday':2, 'Thursday':4}
    dct4={key:value**2 for (key, value) in dct3.items()}
	# dct4 with new values of squared old values created    
    print(dct3)
    print(dct4)
    


main()
