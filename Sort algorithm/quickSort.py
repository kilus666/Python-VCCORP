array=[12,3,4,5,7,3424,6,78,9,354,0,14,5,63,232]
def quickSort(arr, first, last):
    if first < last:
        split = helper(arr, first, last)

        quickSort(arr, first, split-1)
        quickSort(arr, split+1, last)

def helper(arr, first, last):
    leftPointer= first+1
    rightPointer= last 
    pivot= arr[first]

    while leftPointer < rightPointer:
        if arr[leftPointer] < pivot:
            leftPointer +=1
        if arr[rightPointer] > pivot:
            rightPointer -= 1
        if arr[leftPointer] >pivot and arr[rightPointer]< pivot:
            arr[leftPointer], arr[rightPointer]= arr[rightPointer], arr[leftPointer]
            leftPointer +=1
            rightPointer -=1
    
    arr[first], arr[rightPointer]= arr[rightPointer], arr[first]
    return rightPointer

quickSort(array, 0, len(array)-1)
print(array)

'''
    
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

array=[12,3,4,5,7,3424,6,78,9,354,0,14,5,63,232]
quickSort(array)
print(array)
'''