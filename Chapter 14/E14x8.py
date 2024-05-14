# Program E14x8.py
#   merge sort
def merge_sort(arr, low, high):
    if(low<high):
        mid=(low+high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        c=merge_list(arr, low, mid, mid+1, high)
        return c


def merge_list(arr, ll, lr, ul, ur):
    i=ll
    j=ul
    k=ll
    merged=[0,0,0,0,0,0,0,0]
    while(i<=lr and j<=ur):
        if arr[i]<=arr[j]:
           merged[k]=arr[i]
           i=i+1
        else:
            merged[k]=arr[j]
            j=j+1
        k=k+1
    if(i<=lr):
        while(i<=lr):
            merged[k]=arr[i]
            i=i+1
            k=k+1
    if(j<=ur):
        while(j<=ur):
            merged[k]=arr[j]
            j=j+1
            k=k+1
    for k in range(ll, ur+1):
        arr[k]=merged[k]
    return(arr)
def main():
    list1=[33,4,2, 12, 98, 75, 25,11]
    list2=merge_sort(list1, 0,7)
    print('sorted list is ', list2)

main()
        


            
       
