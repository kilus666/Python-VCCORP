arr= [12,232,4545,1,3,34,56,13,14,15]

def bubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        j= 0
        while j< i:
            if arr[j]> arr[j+1]:
                arr[j+1], arr[j]= arr[j], arr[j+1]
            j+=1
bubbleSort(arr)
print(arr)
