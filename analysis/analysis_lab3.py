#!/usr/bin/env python

## Imports
import numpy as np
from scipy.optimize import curve_fit
from matplotlib.pyplot import figure, show, style, rcParams
import scienceplots
import os
import pathlib


## Nice Graphs
style.use(['science'])
rcParams.update({
    "axes.labelsize": 16,  # Axis labels
    "axes.titlesize": 18,  # Title
})

## Functions
def birefringence(theta2, theta1, k, bleed):
    return np.cos(theta1 - theta2)**2 - np.sin(2*theta1)*np.sin(2*theta2)*np.sin(k)**2 + bleed

## Importing data
dataPath = os.path.join(os.getcwd(), '..', 'data', 'Tweaking', 'Lab3', 'lab_3_p2_tweaked.csv')
data = np.loadtxt(dataPath, skiprows=1, encoding='UTF-8', delimiter=',', dtype='float64')
dt = 0.05

dat = []
for col in np.arange(0, 6, 2):
    # Tuple with (time, intensity)
    tup = (data[:, col], data[:, col+1])
    dat.append(tup)
dat = np.array(dat)

# Choosing a run and a spacing between the data points
run = 1

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
frame.plot(rt[ind:], rI[ind:], c='r', label=f'lab run {run+5}')
#frame.set_ylim(5, 20)
#frame.set_xlim(cutoff, 450)
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
I145s= rI[int(0//dt):int(5//dt)].std()

## 140
frame.vlines(85, ymin=0, ymax=100, colors='m')
frame.vlines(104, ymin=0, ymax=100, colors='m')
I140 = rI[int(85//dt):int(104//dt)].mean()
I140s= rI[int(85//dt):int(104//dt)].std()

## 135
frame.vlines(112, ymin=0, ymax=100, colors='y')
frame.vlines(134, ymin=0, ymax=100, colors='y')
I135 = rI[int(112//dt):int(134//dt)].mean()
I135s= rI[int(112//dt):int(134//dt)].std()

## 130
frame.vlines(145, ymin=0, ymax=100, colors='c')
frame.vlines(185, ymin=0, ymax=100, colors='c')
I130 = rI[int(145//dt):int(185//dt)].mean()
I130s= rI[int(145//dt):int(185//dt)].std()

## 125
frame.vlines(205, ymin=0, ymax=100, colors='k')
frame.vlines(235, ymin=0, ymax=100, colors='k')
I125 = rI[int(205//dt):int(235//dt)].mean()
I125s= rI[int(205//dt):int(235//dt)].std()

## Reset to 150 (use this one)
frame.vlines(250, ymin=0, ymax=100, colors='b')
frame.vlines(285, ymin=0, ymax=100, colors='b')
I150 = rI[int(250//dt):int(285//dt)].mean()
I150s= rI[int(250//dt):int(285//dt)].std()

## 155
frame.vlines(300, ymin=0, ymax=100, colors='g')
frame.vlines(310, ymin=0, ymax=100, colors='g')
I155 = rI[int(300//dt):int(310//dt)].mean()
I155s= rI[int(300//dt):int(310//dt)].std()

## 160
frame.vlines(320, ymin=0, ymax=100, colors='m')
frame.vlines(323, ymin=0, ymax=100, colors='m')
I160 = rI[int(320//dt):int(323//dt)].mean()
I160s= rI[int(320//dt):int(323//dt)].std()

## 165
frame.vlines(353, ymin=0, ymax=100, colors='y')
frame.vlines(370, ymin=0, ymax=100, colors='y')
I165 = rI[int(353//dt):int(370//dt)].mean()
I165s= rI[int(353//dt):int(370//dt)].std()

## 170
frame.vlines(380, ymin=0, ymax=100, colors='c')
frame.vlines(395, ymin=0, ymax=100, colors='c')
I170 = rI[int(380//dt):int(395//dt)].mean()
I170s= rI[int(380//dt):int(395//dt)].std()

## 175
frame.vlines(405, ymin=0, ymax=100, colors='k')
frame.vlines(420, ymin=0, ymax=100, colors='k')
I175 = rI[int(405//dt):int(420//dt)].mean()
I175s= rI[int(405//dt):int(420//dt)].std()
"""


frame.set_xlabel('time')
frame.set_ylabel('intensity %')
frame.legend()
frame.grid()
#frame.set_ylim(35, 50)
#frame.set_xticks(np.arange(0, 430, 10))
show()

"""
# Putting everyhing in an array
intensities = np.array([I125, I130, I135, I140, I145, I150, I155, I160, I165, I170, I175])
errors = np.array([I125s, I130s, I135s, I140s, I145s, I150s, I155s, I160s, I165s, I170s, I175s])
theta = np.arange(125, 180, 5) * np.pi / 180
t = np.linspace(125, 175) * np.pi / 180
# normalize
intensities = (intensities - 0.2) / (60-0.2)
errors = errors / (60-0.2)

# Fitting
popt, pcov = curve_fit(birefringence, theta, intensities)
err = np.sqrt(np.diag(pcov))
print(popt)
theta1 = popt[0] * 180 / np.pi
k = popt[1]
Cs0 = k * 4.05*10**(-7) / (np.pi * 0.06)
Cs0err = err[1] * 4.05*10**(-7) / (np.pi * 0.06)
bleed = popt[2]
print(f'theta1 (deg): {theta1} +- {err[0] * 180 / np.pi}')
print(f'C*s0        : {Cs0} +- {Cs0err}')
print(f'bleed       : {bleed} +- {err[2]}')


fig = figure(figsize=(8,6))
frame = fig.add_subplot(111)
frame.errorbar(theta, intensities, yerr=errors, capsize=5, color='r', fmt='.',label='Internal Birefringence')
frame.plot(t, birefringence(t, *popt), label='Fit')

frame.set_title('Unstressed PMMA sample')
frame.set_xlabel(r'$\theta$ (rad)')
frame.set_ylabel('Normalized Intensity')
frame.legend(fontsize=16)
frame.grid()
show()

#fig.savefig('Unstressed.png')
"""
