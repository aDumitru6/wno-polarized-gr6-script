# Quick and dirty data plotter
import matplotlib.pyplot as plt
import numpy as np
import os 
import pathlib

filename = 'Capstone Data.csv'

# Get data
dataPath = os.path.join(os.getcwd(), 'data', filename)
data = np.loadtxt(dataPath, skiprows=1, usecols=[6,7], encoding='UTF-8', delimiter=',', dtype='U')

# Select only the desired data
data = np.array(data[0:7952,:])
data = data.astype('f')

# Plot it
xaxis = np.array(data[:,0]).flatten()
yaxis = np.array(data[:,1]).flatten()

plt.scatter(xaxis,yaxis)
plt.show()
