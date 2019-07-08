from mergeSort import mergeSort
array=[12,3,4,5,7,3424,6,78,9,354,0,14,5,63,232]
mergeSort(array)
print(array)

def binarySearch(arr, value):
    start= 0
    last= len(arr)-1
    while last> start:
        mid= (last+ start)//2
        if arr[mid]> value:
            last= mid
        elif arr[mid]< value:
            start= mid+1
        else:
            print('Found at: '+str(mid))
            break
    if last== start:
        if arr[start]==value:
            print('Found at: '+str(start))
        else:
            print("Not Found")

binarySearch(array,1)