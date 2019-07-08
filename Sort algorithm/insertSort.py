arr= [12,232,4545,1,3,34,56,13,14,15]

def insertSort(arr):
    for i in range(1, len(arr)):
        j= i
        while arr[j-1]> arr[j] and j>0:
            arr[j-1], arr[j]= arr[j], arr[j-1]
            j-=1


insertSort(arr)
print(arr)
