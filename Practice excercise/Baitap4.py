import random
import time
import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np
import copy

# superSet=set()
# class point:

#     def __init__(self, x,y):
#         self.x=x
#         self.y=y
    
#     def __hash__(self):
#         return hash((self.x, self.y))
    
#     def __eq__(self,other):
#         return self.__hash__()== other.__hash__()


#     @classmethod
#     def addPoint(cls,Point):
#         global superSet

#         if isinstance(Point,point):
#                 superSet.add(Point)


# def generatePointHelper(d,center):
#     p= random.random()* 2* math.pi
#     dPoint= math.sqrt(random.random())*d
#     x= dPoint* math.cos(p)+center.x
#     y= dPoint* math.sin(p)+center.y
#     A= point(x,y)
#     return A
    

# def generatePoint(name, d, center, numberOfPoint):
#     start= time.time()
#     print("Start: ", name)
#     while len(superSet)<numberOfPoint:

#             newPoint= generatePointHelper(d,center)
#             point.addPoint(newPoint)
#     print("Finish: ",name)

#     end= time.time()
#     duration= end-start
#     print("Total running time: ", duration)
#     print(" ")

# A=point(800,800)
# B=point(4000,800)
# C=point(2400,2400)

# generatePoint("set1",400,A,8000)
# generatePoint("set2",500,B,18000)
# generatePoint("set3",600,C,30000)



# print("Start writing file\n")
# with open("ouput4.txt", "a") as ouput:
#     for index,i in enumerate(superSet):
#         a= str(index)+". "+ str(i.x)+": "+str(i.y)+"\n"
        
#         ouput.write(a)

# print("Finish output")


# A={"x":800, "y":800} #400
# B={"x":4000, "y":800} #500
# C={"x":2400, "y":2400} #600
    



# Load the data of 30000 points generated before into a dataframe with 2 columns: X, Y
df= pd.DataFrame()
X=[]
Y=[]
with open("ouput4.txt","r") as read:

    for line in read:
        y= line.split(":")[1]
        x= line.split(":")[0].split(".")[1]

        X.append(float(x))
        Y.append(float(y))


df.insert(0,"X",X,False)
df.insert(1,"Y",Y,False)


# Generate 3 random points as the current centroids store in {i: []} format, assign their color
random.seed(100)
randomK= [random.randint(0,29999) for i in range(0,3)]
current_centroids= {i:[df.iloc[k,0], df.iloc[k,1]] for i,k in enumerate(randomK)}
colmap = {0: 'b', 1: 'r', 2: 'g'}

# Function that can determine the closest centroid (eculean distance) for each of 30000 points and assign their color
# As a result of the function, the dataframe will now have 4 main columns: X, Y, closest_centroid, color

def distance_caculate(df, current_centroids):
    for i, k in enumerate(current_centroids):
        df[f"distance_from_{i}"]= (
            np.sqrt(
                (df['X'] - current_centroids[i][0]) ** 2
                + (df['Y'] - current_centroids[i][1]) ** 2
            )
        )
    centroid_columns= [f"distance_from_{i}" for i in current_centroids.keys()]

    df["closest_centroid"]= df.loc[:, centroid_columns].idxmin(axis=1)
    df['closest_centroid'] = df['closest_centroid'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest_centroid'].map(lambda x: colmap[x])
    return df

# Function able to update the current_centroids to the mean of all the points that currently in the same group (same closest centroid)

def update(centroids):
    for i in centroids.keys():
        centroids[i][0]= np.mean(df[df["closest_centroid"]==i]["X"])
        centroids[i][1]= np.mean(df[df["closest_centroid"]==i]["Y"])
    return centroids

# function to run the loop to keep updating the centroids and each point closest centroid
# if each point closest centroid does not change then stop the loop 

def k_mean(df,current_centroids):
    count=0
    while True:
        try:
            closest_centroids= df["closest_centroid"].copy(deep=True)       
            current_centroids = update(current_centroids)
            count+=1
            df= distance_caculate(df,current_centroids)
            if closest_centroids.equals(df['closest_centroid']):
                break
            
        except KeyError:
            df= distance_caculate(df,current_centroids)
    
    return count, df

count, df = k_mean(df, current_centroids)
fig = plt.figure(figsize=(12,8))
for i in current_centroids.keys():
    plt.scatter(*current_centroids[i], color=colmap[i])

plt.scatter(df['X'], df['Y'], color=df['color'], alpha=0.01)

plt.show()
print(count)
