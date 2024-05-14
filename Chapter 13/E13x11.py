# Program E13x11.py
# defining a function in another function
def hi(first_name):
    def greet():
        return "hello "

    result = greet()+first_name
    return result

print(hi("Tushar"))
