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
cutoff = 200
ind = int(cutoff/(dt*spacing))

fig = figure(figsize=(16, 4), tight_layout=True)
frame = fig.add_subplot(111)
frame.plot(rt[ind:], rI[ind:], c='r', label=f'lab run {run+3}')
#frame.set_ylim(5, 20)
#frame.set_xlim(cutoff, 450)

# Setting vertical lines to check where everything is
# taking the mean between the vertical lines to get the intensity of each angle
## 150
frame.vlines(230, ymin=0, ymax=100, colors='b')
frame.vlines(250, ymin=0, ymax=100, colors='b')
I150 = rI[int(230//dt):int(250//dt)].mean()
I150s= rI[int(230//dt):int(250//dt)].std()

## 145
frame.vlines(265, ymin=0, ymax=100, colors='g')
frame.vlines(310, ymin=0, ymax=100, colors='g')
I145 = rI[int(265//dt):int(310//dt)].mean()
I145s= rI[int(265//dt):int(310//dt)].std()

## 140
frame.vlines(325, ymin=0, ymax=100, colors='m')
frame.vlines(360, ymin=0, ymax=100, colors='m')
I140 = rI[int(325//dt):int(360//dt)].mean()
I140s= rI[int(325//dt):int(360//dt)].std()

## 135
frame.vlines(375, ymin=0, ymax=100, colors='y')
frame.vlines(390, ymin=0, ymax=100, colors='y')
I135 = rI[int(375//dt):int(390//dt)].mean()
I135s= rI[int(375//dt):int(390//dt)].std()

## 130
frame.vlines(405, ymin=0, ymax=100, colors='c')
frame.vlines(425, ymin=0, ymax=100, colors='c')
I130 = rI[int(405//dt):int(425//dt)].mean()
I130s= rI[int(405//dt):int(425//dt)].std()

## 125
frame.vlines(435, ymin=0, ymax=100, colors='k')
frame.vlines(445, ymin=0, ymax=100, colors='k')
I125 = rI[int(435//dt):int(445//dt)].mean()
I125s= rI[int(435//dt):int(445//dt)].std()

## 155
frame.vlines(475, ymin=0, ymax=100, colors='g')
frame.vlines(493, ymin=0, ymax=100, colors='g')
I155 = rI[int(475//dt):int(493//dt)].mean()
I155s= rI[int(475//dt):int(493//dt)].std()

## 160
frame.vlines(503, ymin=0, ymax=100, colors='m')
frame.vlines(520, ymin=0, ymax=100, colors='m')
I160 = rI[int(503//dt):int(520//dt)].mean()
I160s= rI[int(503//dt):int(520//dt)].std()

## 165
frame.vlines(530, ymin=0, ymax=100, colors='y')
frame.vlines(550, ymin=0, ymax=100, colors='y')
I165 = rI[int(530//dt):int(550//dt)].mean()
I165s= rI[int(530//dt):int(550//dt)].std()

## 170
frame.vlines(565, ymin=0, ymax=100, colors='c')
frame.vlines(573, ymin=0, ymax=100, colors='c')
I170 = rI[int(565//dt):int(573//dt)].mean()
I170s= rI[int(565//dt):int(573//dt)].std()

## 175
frame.vlines(585, ymin=0, ymax=100, colors='k')
frame.vlines(610, ymin=0, ymax=100, colors='k')
I175 = rI[int(585//dt):int(610//dt)].mean()
I175s= rI[int(585//dt):int(610//dt)].std()



frame.set_xlabel('time')
frame.set_ylabel('intensity %')
frame.legend()
frame.grid()
frame.set_ylim(35, 50)
frame.set_xlim(cutoff, 620)
frame.set_xticks(np.arange(200, 620, 10))
show()

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
frame.errorbar(theta, intensities, yerr=errors, color='r', capsize=5, fmt='.',label='One Weight')
frame.plot(t, birefringence(t, *popt), label='Fit')
#frame.plot(t, birefringence(t, popt[0], -popt[1], popt[2]), c='g')

frame.set_title('PMMA sample stressed by one weight')
frame.set_xlabel(r'$\theta$ (rad)')
frame.set_ylabel('Normalized intensity')
frame.legend(fontsize=16)
frame.grid()
show()

fig.savefig('One_block.png')
