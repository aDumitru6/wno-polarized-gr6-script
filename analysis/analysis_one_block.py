#!/usr/bin/env python

## Imports
import numpy as np
from matplotlib.pyplot import figure, show
import os
import pathlib

## Importing data
dataPath = os.path.join(os.getcwd(), '..', 'data', 'Tweaking', 'Lab2', 'Lab_2_tweaked.csv')
data = np.loadtxt(dataPath, skiprows=1, encoding='UTF-8', delimiter=',', dtype='float64')
dt = 0.05

dat = []
for col in np.arange(0, 20, 2):
    # Tuple with (time, intensity)
    tup = (data[:, col], data[:, col+1])
    dat.append(tup)
dat = np.array(dat)

# Choosing a run and a spacing between the data points
run = 8
## runs go from 0 to 9
## In the lab notebook, the corrsepond to runs 4 through 12 (from sesh 2)
## subtract 4 from the lab run to get the code run
## WARNING: Ignore run 6. Lab runs 10, 11 and 12, correspond to 7, 8, 9

spacing = 1 # only showing every n-th point so we render less
rt = []
rI = []
for i in np.arange(dat.shape[2] // spacing):
    rt.append(dat[run][0][i*spacing])
    rI.append(dat[run][1][i*spacing])
rt = np.array(rt)
rI = np.array(rI)
print(f'run: {run}\nspacing: {spacing}')

# Matplotlib type shit
cutoff = 0
ind = int(cutoff/(dt*spacing))

fig = figure(figsize=(16, 4), tight_layout=True)
frame = fig.add_subplot(111)
frame.plot(rt[ind:], rI[ind:], c='r', label=f'lab run {run+4}')
#frame.set_ylim(5, 20)
#frame.set_xlim(cutoff, 450)

show()
"""
# Setting vertical lines to check where everything is
# taking the mean between the vertical lines to get the intensity of each angle
## 150 (ignore this one)
frame.vlines(0, ymin=0, ymax=100, colors='b')
frame.vlines(5, ymin=0, ymax=100, colors='b')
## 145
frame.vlines(20, ymin=0, ymax=100, colors='g')
frame.vlines(50, ymin=0, ymax=100, colors='g')

I145 = rI[int(0//dt):int(5//dt)].mean()
## 140
frame.vlines(85, ymin=0, ymax=100, colors='m')
frame.vlines(104, ymin=0, ymax=100, colors='m')

I140 = rI[int(85//dt):int(104//dt)].mean()
## 135
frame.vlines(112, ymin=0, ymax=100, colors='y')
frame.vlines(134, ymin=0, ymax=100, colors='y')

I135 = rI[int(112//dt):int(134//dt)].mean()
## 130
frame.vlines(145, ymin=0, ymax=100, colors='c')
frame.vlines(185, ymin=0, ymax=100, colors='c')

I130 = rI[int(145//dt):int(185//dt)].mean()
## 125
frame.vlines(205, ymin=0, ymax=100, colors='k')
frame.vlines(235, ymin=0, ymax=100, colors='k')

I125 = rI[int(205//dt):int(235//dt)].mean()
## Reset to 150 (use this one)
frame.vlines(250, ymin=0, ymax=100, colors='b')
frame.vlines(285, ymin=0, ymax=100, colors='b')

I150 = rI[int(250//dt):int(285//dt)].mean()
## 155
frame.vlines(300, ymin=0, ymax=100, colors='g')
frame.vlines(310, ymin=0, ymax=100, colors='g')

I155 = rI[int(300//dt):int(310//dt)].mean()
## 160
frame.vlines(320, ymin=0, ymax=100, colors='m')
frame.vlines(323, ymin=0, ymax=100, colors='m')

I160 = rI[int(320//dt):int(323//dt)].mean()
## 165
frame.vlines(353, ymin=0, ymax=100, colors='y')
frame.vlines(370, ymin=0, ymax=100, colors='y')

I165 = rI[int(353//dt):int(370//dt)].mean()
## 170
frame.vlines(380, ymin=0, ymax=100, colors='c')
frame.vlines(395, ymin=0, ymax=100, colors='c')

I170 = rI[int(380//dt):int(395//dt)].mean()
## 175
frame.vlines(405, ymin=0, ymax=100, colors='k')
frame.vlines(420, ymin=0, ymax=100, colors='k')

I175 = rI[int(405//dt):int(420//dt)].mean()


frame.set_xlabel('time')
frame.set_ylabel('intensity %')
frame.legend()
frame.grid()
frame.set_ylim(35, 50)
frame.set_xticks(np.arange(0, 430, 10))
show()

# Putting everyhing in an array
intensities = np.array([I125, I130, I135, I140, I145, I150, I155, I160, I165, I170, I175])
theta = np.arange(125, 180, 5) * np.pi / 180
# normalize
intensities = intensities / intensities.max()

fig = figure(figsize=(16,9))
frame = fig.add_subplot(111)
frame.scatter(theta, intensities, label='internal birefringence')

frame.set_xlabel('theta (rad)')
frame.set_ylabel('Normalized intensity')
frame.legend()
frame.grid()
show()
"""
