
import random
import time
def ran(start, end, num):
    SET=set([])
    for i in range(num):
        SET.add(random.randint(start,end))
    return SET
percent=0
start= time.time()
while percent<0.05:
    set1= ran(0,3000000,2000000)
    set2= ran(1000000, 4000000,2000000)
    Intersection= set1.intersection(set2)
    percent= len(Intersection)/2000000
end= time.time()
duration= end-start
print("Time create the set1, set2: ",duration)


start= time.time()
intersect= set1.intersection(set2)
union= set1.union(set2)
end= time.time()
duration= end-start
print("Time to intersect and union", duration)

