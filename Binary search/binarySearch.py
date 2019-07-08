from mergeSort import mergeSort
array=[12,3,4,5,7,3424,6,78,9,354,0,14,5,63,232]
mergeSort(array)
print(array)
def binarySearch(arr,value):
    _binarySearch(arr, 0, len(arr)-1, value)

def _binarySearch(arr, start, last, value):
    if last> start:
        mid= (last+start)//2
        if arr[mid] == value:
            print("Found at: "+ str(mid+1))
        elif value< arr[mid]:
            _binarySearch(arr, start, mid, value)
        else:
            _binarySearch(arr, mid+1,last, value)
    else:
        if arr[start]== value:
            print('Found at start')
        else:
            print("Not Found")


binarySearch(array,4)



