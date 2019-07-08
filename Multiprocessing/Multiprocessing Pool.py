import time 
from multiprocessing import Pool

def sumSquare(numbers):
    s=0
    for i in range(numbers):
        s+= i*i 
    return s

def sumSquareWithMP(numbers):
    startTime=time.time()
    p= Pool()
    result= p.map(sumSquare, numbers)
   
    p.close()
    p.join()

    endTime=time.time()-startTime
    print(f"Processing {len(numbers)} numbers took {endTime} time using multiprocessing.")

def sumSquarenoMP(numbers):
    startTime=time.time()
    result=[]
    for i in numbers:
        result.append(sumSquare(i))
    endTime= time.time()- startTime
    print(f"Processing {len(numbers)} numbers took {endTime} time using normal.")
if __name__== "__main__":
    numbers= range(10000)
    sumSquareWithMP(numbers)
    sumSquarenoMP(numbers)

