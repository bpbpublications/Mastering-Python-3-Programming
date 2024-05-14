# program E11x18.py
# pickling
import pickle
def main():
    x=['This', 'is', 'pickling', 'problem']
    outfile=open("b2", 'wb') # open for writing
    pickle.dump(x,outfile)
    outfile.close()
    infile=open("b2", 'rb')
    y = pickle.load(infile)
    print(y)
    infile.close()
main()
