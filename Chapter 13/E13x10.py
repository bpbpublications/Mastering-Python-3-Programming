# Program E13x10.py
# function passed as parameters to other functions
def hi(first_name):
    return "hello " +first_name
def other(fun):
    arg="Tushar"
    return fun(arg)

print(other(hi))
