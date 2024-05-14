'''swap_case.py'''
# to change case
def swap(alpha):
    if alpha >='a' and alpha<='z' :
        y=ord(alpha)
        return(chr(y-32))
    elif alpha >='A' and alpha<='Z' :
        y=ord(alpha)
        return(chr(y+32))
