import random
import multiprocessing
import time

superList=[]
superDict={}

class point:

    def __init__(self, x,y):
        self.x=x
        self.y=y
    
    @classmethod
    def addPoint(cls,Point):
        global superList
        if isinstance(Point,point):
            if len(superList)!=0:
                count=0         
                for i in superList:
                    if i.x==Point.x and i.y==Point.y:
                        count=1
                        pass
                if count==0:
                    superList.append(Point)

            else:
                superList.append(Point)


def generatePointHelper(d,center):
    
    distance=99999
    while distance>d:
        x= random.randint(100,5000)
        y= random.randint(100,5000)
        distance= ((x-center.x)**2+(y-center.y)**2)**(1/2)
    A= point(x,y)
    return A

def generatePointSetA(number):
    subList= []
    while len(subList) < number:
        newPoint= generatePointHelper(400,A)
        subList.append(newPoint)
    return subList

var= [3000,3000,3000,3000,3000,3000]
A=point(800,800)
B=point(4000,800)
C=point(2400,2400)

def addPoint(Point):
        global superList
        if isinstance(Point,point):
            if len(superList)!=0:
                count=0         
                for i in superList:
                    if i.x==Point.x and i.y==Point.y:
                        count=1
                        pass
                if count==0:
                    superList.append(Point)

            else:
                superList.append(Point)
def addPointDict(Point):
    global superDict
    if isinstance(Point, point):
        if len(superDict)==0:
            superDict[Point.x]= Point.y
        else:
            try:
                if superDict[Point.x]== Point.y:
                    pass
                else:
                    superDict[Point.x]= Point.y
            except KeyError:
                superDict[Point.x]= Point.y


if __name__=="__main__":
    
    start= time.time()
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result= pool.map(generatePointSetA,var)
    pool.close()
    end1= time.time()
    while len(superDict)<8000:
        for i in result:
            for j in i:
                addPointDict(j)

    end= time.time()
    duration1= end1-start
    duration=end-start
    print(duration1,"\n")
    print(duration)
    print(superDict)
    

