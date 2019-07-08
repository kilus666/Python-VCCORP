import codecs
import re
import os
import json
import sqlite3
import pickle
import time
from collections import Counter
import multiprocessing


superList={}
curr= 999999
Id= None
SmallestTen= {}
def WordCount(fileName, encoding):
    dictOfWord={}
    try:
        f = codecs.open(fileName, encoding= encoding)
        for line in f:
            a= re.split("\W",line)
            for word in a:
                try:
                    dictOfWord[word]+=1
                except KeyError:
                    dictOfWord[word]=1
    
    except Exception:
        with open(fileName, "r") as f:
            for line in f:
                a= re.split("\W",line)
            for word in a:
                try:
                    
                    dictOfWord[word]+=1
                except KeyError:
                    dictOfWord[word]=1
    return dictOfWord
    
def writeFile(data):
    for word, count in data.items():
        try:
            superList[word]+=count
        except Exception:
            superList[word]= count

def findSmallest(data):
    global curr
    global Id
    global SmallestTen
    while len(SmallestTen)<10:
        
        for i, k in data.items():
            if k<= curr:
                curr= k
                Id= i
        del data[Id]
        SmallestTen[Id]= curr
        curr=9999
        Id= None
        findSmallest(data)


# if __name__== "__main__":
print("Start without multiprocessing")
print(" ")
start= time.time()
currentPath= os.getcwd()
path= os.path.join(currentPath,"input_3")
for root, dirs, files in os.walk(path):

        for file in files:
            filePath= os.path.join(root, file)
            print(filePath)
            A= WordCount(filePath, "utf-8")
            writeFile(A)
# with open("SuperDict.pickle", "wb") as superDict:
#         pickle.dump(superList, superDict)

print("Top 10 common word: ",dict(Counter(superList).most_common(10)))
findSmallest(superList)   
print("Top 10 least common word: ",SmallestTen)

end= time.time()
duration= end-start
print(" ")
print("End without multiprocessing")
print(" ")
print("Total run time: ",duration)
print(" ")

# os.remove("SuperDict.pickle")
# try:
#     with open("SuperDict.pickle", "rb") as superDict:
#         superList= pickle.load(superDict)
# except Exception:
#     print("Xoa file thanh cong")






            

            
            
            