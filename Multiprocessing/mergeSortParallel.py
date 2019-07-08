from multiprocessing import *
import time
import random
import math

#create random list

myList=[]
for i in range (0, 1000000):
    listValue= random.randint(1, 10000000)
    myList.append(listValue)

def mergeSort(arr):
    l=len(arr)
    if l==1:
        return arr

    mid= l//2
    # Devide the array into 2 sublist
    # Recursive for further devision
    left= mergeSort(arr[:mid])
    right= mergeSort(arr[mid:])
    
    # Merge 2 sublists
    return merge(left, right)


    

def merge(*args):
        left, right = args[0] if len(args) == 1 else args
        i=k=0
        merged=[]
        while i<len(left) and k< len(right):
            if left[i]< right[k]:
                merged.append(left[i])
                i+=1
            else: 
                merged.append(right[k])
                k+=1
        
        if i== len(left):
            merged.extend(right[k:])
            
        if k== len(right):
            merged.extend(left[i:])
            
        return merged

def mergeParallel(data):

    pool = Pool(6)
    size = int(math.ceil(float(len(data)) / 6))
    data = [data[i * size:(i + 1) * size] for i in range(6)]
    data = pool.map(mergeSort, data)

    while len(data) > 1:

        extra = data.pop() if len(data) % 2 == 1 else None
        data = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
        data = pool.map(merge, data) + ([extra] if extra else [])
    return data[0]

if __name__=="__main__":
    
    for sort in mergeSort, mergeParallel:
        startTime= time.time()
        dataSorted= sort(myList)
        Duration= time.time()- startTime
        print (sort.__name__, Duration)


