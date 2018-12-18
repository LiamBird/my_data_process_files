import os
import glob
import pandas as pd
import numpy as np
from numpy import median
from matplotlib import pyplot as plt
import plotly.plotly as py
import plotly.tools as tls

##path = r'C:\Users\laure\OneDrive - University Of Cambridge\DATA\(0-0-1)(0-20)T\SCap\processed\collected_data'
##path = r'C:\Users\laure\OneDrive - University Of Cambridge\DATA\(0-0-1)(0-0)cP\processed\caprem'
##path= r'C:\Users\laure\Dropbox\DATA\SCap\(0-0-1)(0-10)T\processed\SCap'
##path = r'C:\Users\laure\Dropbox\DATA\SCap\(0-0-1)(0-0).P\processed\SCap'
##path = r'C:\Users\laure\Dropbox\DATA\SCap\(0-0-1)(0-10)T\processed\SCap'
##path = r'C:\Users\laure\Dropbox\DATA\SCap\(0-0-1)(0-20)T\processed\SCap'
##path = r'C:\Users\laure\Dropbox\DATA\SCap\(0-0-1)(10-0)P\processed\SCap'
path = r'C:\Users\laure\Dropbox\DATA\SCap\(0-0-1)(10-0)T\processed\SCap'
discharge = np.load(path+'.npy')
    
cycles = range(len(discharge))

ax = plt.figure(1)

plotdat = discharge[:, 2]
lastcyc = (~np.isnan(plotdat)).cumsum(0).argmax(0)
x = cycles[1:lastcyc]
y = discharge[1:lastcyc, 2]

sample1 = plt.plot(cycles, discharge[:, 0], ls='None', marker='o', color='black')
sample2 = plt.plot(cycles, discharge[:, 1], ls='None', marker='o', color='red')
sample3 = plt.plot(cycles, discharge[:, 2], ls='None', marker='o', color='blue')
##sample4 = plt.plot(x, y, ls='None', marker='o', color='k')
##sample5 = plt.plot(cycles, discharge[:, 4], ls='None', marker='o', color='c')

plt.xlabel('Cycle number')
plt.ylabel('Gravimetric Capacity (mAh/g)')
plt.tick_params(axis='y', which='both', direction='in', labelright=False, right=True)
plt.minorticks_on()
plt.tick_params(which='both', direction='in', right=True, left=True, bottom=True, top=True)
##plt.ylim([0, 100])
