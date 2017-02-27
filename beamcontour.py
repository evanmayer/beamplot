# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 18:11:54 2017

@author: Evan
"""

import numpy as np
from scipy import loadtxt
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

phi, theta, db = (
                  loadtxt("filename.csv", 
                          delimiter = ",", unpack=True, skiprows=1))
xsize = np.argmax(phi)+1
ysize = max(theta) - min(theta) + 1
phi = phi * np.pi / 180.
theta = theta * np.pi / 180.
db -= min(db)

phi = np.reshape(phi, (ysize, xsize))
theta = np.reshape(theta, (ysize, xsize))
db = np.reshape(db, (ysize, xsize))

x = db * np.sin(theta) * np.cos(phi)
y = db * np.sin(theta) * np.sin(phi)
z = db * np.cos(theta)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_xlabel('Y')
ax.plot_surface(x,y,z, rstride=3, cstride=6, cmap=plt.get_cmap('jet'))
plt.show()
