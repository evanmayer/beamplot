# beamplot
Direct pipeline from HFSS Plot3D Export File (.csv) to matplotlib 3D plot.

HFSS exports its 3D beam map data in a way that is...not great, so this code break it down into something usable by matplotlib's 3D functions:
X, Y, and Z arrays that can be passed to plot_surface to recreate the beam map, for manipulation and beautification using python.
Step-by-step:
- read in cols from hfss's .csv export file
- reshape these arrays to be matrices: phi values are split into rows, starting each successive row after the max value of phi is reached.
  this will be the number of columns in the matrix.
  theta values are split into rows by finding the limits of theta travel on the plot: this will be the number of rows in the matrix. 
  I suppose this reshaping assumes dtheta in the radiation boundary setup in HFSS = 1degree: I will investigate.
  db values are flattened accordingly.
- the typical transformation from spherical coordinates to 3D cartesian is done
- values are plotted using plot_surface.
