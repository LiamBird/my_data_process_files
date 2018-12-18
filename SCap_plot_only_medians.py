import os
import glob
import pandas as pd
import numpy as np
from numpy import median, nanmedian
from matplotlib import pyplot as plt
import plotly.plotly as py
import plotly.tools as tls

##CMK_SPCB = r'C:\Users\laure\OneDrive - University Of Cambridge\DATA\(0-0-1)(0-20)T\SCap\processed\collected_data'
CMK_SPCB = r'C:\Users\laure\OneDrive - University Of Cambridge\DATA\(0-0-1)(0-20)T\SCap\processed\caprem'
CMK_CMK = r'C:\Users\laure\OneDrive - University Of Cambridge\DATA\(0-0-1)(0-0)cP\processed\caprem'
dischargeA = np.load(CMK_SPCB+'.npy')
dischargeB = np.load(CMK_CMK+'.npy')
    
cycA = len(dischargeA)
cycB = len(dischargeB)

yA = np.zeros(shape=len(dischargeA), dtype=float)
Aerr = np.zeros(shape=(2, len(dischargeA)), dtype=float)
yB = np.zeros(shape=len(dischargeB), dtype=float)
Berr = np.zeros(shape=(2, len(dischargeB)), dtype=float)


for i in range(len(dischargeA)):
    yA[i] = nanmedian(dischargeA[i, :])
    Aerr[0, i] = max(dischargeA[i, :])
    Aerr[1, i] = min(dischargeA[i, :])

for i in range(len(dischargeB)):
    yB[i] = nanmedian(dischargeB[i, :])
    Berr[0, i] = max(dischargeB[i, :])-yB[i]
    Berr[1, i] = yB[i]-min(dischargeB[i, :])

Aerr_red = np.zeros(shape=(2, Aerr.shape[1]), dtype=float)
for i in range(0, Aerr.shape[1], 10):
    Aerr_red[0, i] = Aerr[0, i]

Berr_red = np.zeros(shape=(2, Berr.shape[1]), dtype=float)
for i in range(0, Berr.shape[1], 10):
    Berr_red[0, i] = Berr[0, i]
    

##Aerr_red = np.zeros(shape=(2, Aerr.shape[1]), dtype=float)
##for i in range(0, len(Aerr), 10):
##    Aerr_red[i] = Aerr[i]
    

ax = plt.figure(1)

##plotdat = discharge[:, 3]
##lastcyc = (~np.isnan(plotdat)).cumsum(0).argmax(0)

CMK_SPCB_plot = plt.plot(range(0, cycA), yA, ls='None', marker='o')
##CMK_CMK_plot = plt.plot(range(0, cycB), yB, ls='None', marker='o')
##CMK_SPCB_plot = plt.errorbar(range(0, cycA), yA, Aerr, ls='None', marker='o')
##CMK_CMK_plot = plt.errorbar(range(0, cycB), yB, Berr, ls='None', marker='o')

plt.ylim([0, 100])
plt.show()

##x = cycles[1:lastcyc]
##y = discharge[1:lastcyc, 3]

##sample1 = plt.plot(cycles, discharge[:, 0], ls='None', marker='o', color='black')
##sample2 = plt.plot(cycles, discharge[:, 1], ls='None', marker='o', color='red')
##sample3 = plt.plot(cycles, discharge[:, 2], ls='None', marker='o', color='blue')
##sample4 = plt.plot(x, y, ls='None', marker='o', color='k')
##sample5 = plt.plot(cycles, discharge[:, 4], ls='None', marker='o', color='c')

##plt.xlabel('Cycle number')
##plt.ylabel('Gravimetric Capacity (mAh/g)')
##plt.tick_params(axis='y', which='both', direction='in', labelright=False, right=True)
##plt.minorticks_on()
##plt.tick_params(which='minor', direction='in', right=True, left=True, bottom=True, top=True)
##plt.ylim([0, 100])
