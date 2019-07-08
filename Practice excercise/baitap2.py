import codecs
import re

def WordCount(fileName, encoding):
    f = codecs.open(fileName, encoding= encoding)
    dictOfWord={}
    for line in f:
        a= re.split("\W",line)
        for word in a:
            try:
                
                dictOfWord[word]+=1
            except KeyError:
                dictOfWord[word]=1
    return dictOfWord
a=WordCount("01.txt", encoding="utf-8")

print(a)