# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 18:11:54 2017

@author: Evan Mayer
"""

import numpy as np
from scipy import loadtxt
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

phi, theta, db = (
                  loadtxt("filename.csv", 
                          delimiter = ",", unpack=True, skiprows=1))
# get size of theta and phi sweeps
xsize = np.argmax(phi)+1
ysize = int(max(theta) - min(theta) + 1)
# convert arrays to radians
phi = phi * np.pi / 180.
theta = theta * np.pi / 180.
# ensure all power values are positive, and normalize 
db -= min(db)
db = db/(max(db))
# reshape raw data into X,Y,Z matrices
phi = np.reshape(phi, (ysize, xsize))
theta = np.reshape(theta, (ysize, xsize))
db = np.reshape(db, (ysize, xsize))
#convert to polar
x = db * np.sin(theta) * np.cos(phi)
y = db * np.sin(theta) * np.sin(phi)
z = db * np.cos(theta)

# color dimension: allows plotting color as a func of radius instead of z
# http://stackoverflow.com/a/32480062
color_dim = np.sqrt(x**2 + y**2 + z**2)
cmax = color_dim.max() # sets normalization of color scale
cmin = color_dim.min()
minc, maxc = color_dim.min(), color_dim.max()
norm = mpl.colors.Normalize(cmin, cmax)
m = plt.cm.ScalarMappable(norm=norm, cmap='magma')
m.set_array([])
fcolors = m.to_rgba(color_dim) # face colors of surface

fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Normalized Gain X')
ax.set_ylabel('Normalized Gain Y')
ax.set_zlabel('Normalized Gain Z')
ax.set_title('Simulated Beam Pattern\nLensed Dual-Slot Antenna,' +
                '$f \equal \, 220$ GHz')

p = ax.plot_surface(x,y,z, rstride=1, cstride=1, 
                    facecolors=fcolors, vmin = cmin, vmax = cmax,  
                    shade=False)
p.set_edgecolor('k')
cb = fig.colorbar(m, norm=norm, shrink = 0.5)

plt.savefig('220GHzideal.png', format = 'png', dpi=750)
plt.savefig('220GHzideal.eps', format = 'eps', dpi=1000)
plt.show()
