#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 20:14:16 2020

@author: rogith
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("data.txt", delimiter= '\s+',header=None)

X = df.iloc[:,:].values

from sklearn.cluster import DBSCAN 

# Load data in X 
db = DBSCAN(eps=0.3, min_samples=10).fit(X) 
core_samples_mask = np.zeros_like(db.labels_, dtype=bool) 
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_ 

# Number of clusters in labels, ignoring noise if present. 
n_clusters_ = len(set(labels)) 

print(labels) 

# Black removed and is used for noise instead. 
unique_labels = set(labels) 
colors = ['y', 'b', 'g', 'r'] 
print(colors) 
for k, col in zip(unique_labels, colors): 
	if k==-1:
         col = 'k
	class_member_mask = (labels == k) 

	xy = X[class_member_mask & core_samples_mask] 
	plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, 
									markeredgecolor='k', 
									markersize=6) 

	xy = X[class_member_mask & ~core_samples_mask] 
	plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, 
									markeredgecolor='k', 
									markersize=6) 

plt.title('number of clusters of ggod data: %d' %n_clusters_) 
plt.show() 
