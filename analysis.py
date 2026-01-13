#!/usr/bin/env python

## Imports
import numpy as np
from matplotlib.pyplot import figure, show
import os
import pathlib

## Importing data
dataPath = os.path.join(os.getcwd(), 'data', 'Capstone Data robert.csv')
data = np.loadtxt(dataPath, skiprows=1, encoding='UTF-8', delimiter=',', dtype='float64')
dt = 0.02

dat = []
for col in np.arange(0, 9, 2):
    tup = (data[:, col], data[:, col+1])
    dat.append(tup)
dat = np.array(dat)


# Choosing a run and a spacing between the data points
## RUNS 2 AND 3 ARE USELESS, 4 is done by Andrei (magic). I will work on 1 hihih
run = 1 # runs go from 0 to 4
spacing = 1 # only showing every n-th point so we render less
rt = []
rI = []
for i in np.arange(23713 // spacing):
    rt.append(dat[run][0][i*spacing])
    rI.append(dat[run][1][i*spacing])
rt = np.array(rt)
rI = np.array(rI)
print(f'run: {run}\nspacing: {spacing}')

# Matplotlib type shit
cutoff = 0
ind = int(cutoff/(dt*spacing))

fig = figure(figsize=(16, 9), tight_layout=True)
frame = fig.add_subplot(111)
frame.scatter(rt[ind:], rI[ind:], s=0.1, c='r', label=f'run 1')
#frame.set_ylim(5, 20)
#frame.set_xlim(cutoff, 450)

# Setting vertical lines to check where everything is
frame.vline(



frame.set_xlabel('time')
frame.set_ylabel('intensity %')
frame.legend()
frame.grid()
show()
