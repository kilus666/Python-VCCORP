
import pandas as pd
import matplotlib.pyplot as plt



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

from sklearn.cluster import KMeans

kmeans= KMeans(n_clusters= 3)
kmeans.fit(df)
labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

colmap= {1:"r",2:"g",3:"b"}


colors = list(map(lambda x: colmap[x+1], labels))
fig = plt.figure(figsize=(12, 8))
plt.scatter(df['X'], df['Y'], color=colors, alpha=0.01)

for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colmap[idx+1])

plt.show()