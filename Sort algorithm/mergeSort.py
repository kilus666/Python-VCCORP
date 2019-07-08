arr= [12,232,4545,1,3,34,56,13,14,15]
def mergeSort(arr):
    if len(arr)>1:
        l= len(arr)
        mid= l//2
        # Devide the array into 2 sublist
        left= arr[:mid]
        right= arr[mid:]
        # Recursive for further devision
        mergeSort(left)
        mergeSort(right)

        i=k=j=0
        # Merge 2 sublists
        while i<len(left) and k< len(right):
            if left[i]< right[k]:
                arr[j]= left[i]
                i+=1
            else: 
                arr[j]= right[k]
                k+=1
            j+=1
        
        while i< len(left):
            arr[j]=left[i]
            i+=1
            j+=1
        
        while k< len(right):
            arr[j]= right[k]
            k+=1
            j+=1

mergeSort(arr)
print(arr)        