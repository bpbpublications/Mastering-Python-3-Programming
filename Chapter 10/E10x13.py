# program E10x13.py
# generator
def Even_gen():
    num = 100
    print('This is printed first')
    # Generator function contains yield statements
    yield num

    num-= 2
    print('This is printed second')
    yield num

    num-= 2
    print('This is printed at last')
    yield num
  
for item in Even_gen():
    print(item)

