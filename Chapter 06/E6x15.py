# Program E6x15.py
# Keyword arguments

def fun(**kwargs):
    print("\nData type of argument:",type(kwargs))

    for key, value in kwargs.items():
        print("{} is {}".format(key,value))
def main():
    fun(Firstname="ram", Age=27, Phone=123456)
    fun(Firstname="Sita", Lastname="ram", Country="India", Age=25, Phone=43210)
main()
