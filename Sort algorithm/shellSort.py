

def shellSort(arr):

    gap= len(arr)//2
    
    while gap >= 1:
        gapFixInsert(arr, gap)
        gap//=2


def gapFixInsert(arr,gap):
    
    for i in range(0, len(arr),gap):
        j=i
        while j >0 and arr[j-gap]> arr[j]:
            arr[j],arr[j-gap]= arr[j-gap],arr[j]
            j-=gap

alist = [12,232,4545,1,3,34,56,13,14,15,67,45,12]
shellSort(alist)
print(alist)


