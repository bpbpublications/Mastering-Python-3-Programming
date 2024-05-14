# Program E6x18.py
# Towers of Hanoi program
def xfer(n, s,  d, temp):   
        if(n==1):
            print('transfer disk ', n, 'from ',s, 'to ',d)
        else:       
                # transfer n-1 disks from source to temp
            xfer(n-1,s,temp,d)
                 # transfer n from source to destination
            print('transfer disk ', n, 'from ',s, 'to ',d)
		# transfer n-1 disks from  temp to destination	
            xfer(n-1, temp, d, s)
        

def main():
    n=eval(input('enter the number of disks to play with: '))
    print('The moves follow: ')
    xfer(n,'s', 'd','t')

main()
