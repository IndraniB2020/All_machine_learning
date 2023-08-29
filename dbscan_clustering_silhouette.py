# -*- coding: utf-8 -*-
"""dbscan_clustering

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mBYyuzld5fz0FPUauKxQ437MeEc9exN0
"""

###5 points to remember- 1.core point, 2.Border point, 3.Noise/outliers 4.Epsilon 5.min_points
####elbow method/silhoutte method - which method to choose
###dbscan - Density-based Spatial Clustering of Applications, comes under unsupervised algo
###Epsilon - is the radius from the core to the border of the circle
###Noise point is an outlier
####works not well with clusters of varying densities.
##dbscan works well with the noise/ works best with handling outliers
###metrics - euclidean distance or manhattan distance
#sklearn.cluster.dbscan    ##all independent features in unsuprevised

import pandas as pd
import numpy as np

from google.colab import drive
drive.mount('/content/drive/')
df = pd.read_csv("/content/drive/MyDrive/Fakedata/Mall_customers.csv")

x = df.iloc[:, [3,4]].values

##Apply dbscan algo
from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=3, min_samples=4)

##Fitiing the model
model = dbscan.fit(x)

labels = model.labels_   #display(labels)

from sklearn import metrics

##identifying the points which makes up core points
sample_cores=np.zeros_like(labels,dtype=bool)   #display(sample_cores)
sample_cores[dbscan.core_sample_indices_]=True

##calculating clusters numbers
n_clusters = len(set(labels))-(1 if -1 in labels else 0)
display(n_clusters)

print(metrics.silhouette_score(x, labels))