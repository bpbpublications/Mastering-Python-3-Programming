# Program E9x8.py
# overloading == operator
class Length:
    def __init__(self, ft=0, inch=0):
        self._ft=ft
        self._inch=inch

    def __eq__(self, other):
        if self._ft==other._ft and self._inch==other._inch:
            return True
        else:
            return False
def main():
    len1=Length(3, 4)
    len2=Length(4,5)
    len3=len2
    if len1==len2:
        print("objects len1 and len2 are equal")
    else:
        print('objects len1 and len2 are not same')
    if len2==len3:
        print("objects len2 and len3 are equal")
    else:
        print('objects len2 and len3 are not same')

    if len1 is len2:
        print('len1 and len2 are pointing to same object')
    else:
        print('len1 and len2 are NOT pointing to same object')
    if len2 is len3:
        print('len2 and len3 are pointing to same object')
    else:
        print('len2 and len3 are NOT pointing to same object')

main()
