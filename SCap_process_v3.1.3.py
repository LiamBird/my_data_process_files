import os
import glob
import pandas as pd
import numpy as np
from numpy import median
from matplotlib import pyplot as plt
import plotly.plotly as py
import plotly.tools as tls

from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

majorLocator = MultipleLocator(20)
majorFormatter = FormatStrFormatter('%d')
minorLocator = MultipleLocator(5)

mass = [1.8722, 1.2329, 1.8011, 3.6468, 0.2251, 0.2251]
massg = np.empty(shape=(len(mass)), dtype=object)
for j in range(len(mass)):
    massg[j] = mass[j]/1000

##path = r'C:\Users\laure\OneDrive - University Of Cambridge\DATA\(0-0-1)(0-20)T\SCap'
path = r'C:\Users\laure\OneDrive - University Of Cambridge\DATA\PlasmaApp_init'
all_files = glob.glob(os.path.join(path, "*.txt"))

data_imp = (pd.read_csv(f, delimiter='\t') for f in all_files)
rawimp = pd.concat(data_imp, ignore_index=True)

rawimp = np.asarray(rawimp)

bd=[]

for i in range(len(rawimp)):
    if rawimp[i, 0] == 1:
        bd.append(i)

bd.append(len(rawimp))

bdl = np.zeros(shape=(len(bd)-1), dtype=int)
for i in range(len(bd)-1):
    bdl[i] = bd[i+1]-bd[i]

data = np.empty(shape=(max(bdl), 4, len(bdl)), dtype=object)
discharge = np.empty(shape=(max(bdl), len(bdl)), dtype=object)

##data[range(0,bdl[0]), :, 0] = rawimp[range(0,bd[1]), :]
##data[range(0, bdl[1]), :, 1] = rawimp[range(bd[1], bd[2]), :]
##data[range(0, bdl[2]), :, 2] = rawimp[range(bd[2], bd[3]), :]


for i in range(len(bdl)):
    data[range(0, bdl[i]), :, i] = rawimp[range(bd[i], bd[i+1]), :]

for i in range(max(bdl)):
    for j in range(len(bdl)):
        discharge[i, j] = data[i, 2, j]/massg[j]

## Cycles vs capacity plot
cycCap = plt.figure(1)
x = range(0, len(data))

yCO1 = np.empty(shape=(len(discharge)), dtype=object)
yC6 = np.empty(shape=(len(discharge)), dtype=object)
yC7 = np.empty(shape=(len(discharge)), dtype=object)
for i in range(len(discharge)):
    yCO1[i] = median([discharge[i, 4], discharge[i, 5]])
    yC6[i] = median([discharge[i, 0], discharge[i, 1]])
    yC7[i] = median([discharge[i, 2], discharge[i, 3]])
##y0 = discharge[:, 0]
##y1 = discharge[:, 1]
##y2 = discharge[:, 2]
##y3 = discharge[:, 3]
##y4 = discharge[:, 4]
##y5 = discharge[:, 5]
##
##scap0 = plt.plot(x, y0, 'x', color='red', label='C6')
##scap1 = plt.plot(x, y1, 'x', color='red', label='C6')
##scap2 = plt.plot(x, y2, 'x', color='blue', label='C7')
##scap3 = plt.plot(x, y3, 'x', color='blue', label='C7')
##scap4 = plt.plot(x, y4, 'x', color='green', label='CO1')
##scap5 = plt.plot(x, y5, 'x', color='green', label='CO1')

scapO1 = plt.plot(x, yCO1, color='black', marker='o', ls='none', label='CO1')
scapc6 = plt.plot(x, yC6, color='red', marker='o', ls='none', label='C6')
scapc7 = plt.plot(x, yC7, color='blue', marker='o', ls='none', label='C7')

plt.xlabel('Cycle number')
plt.ylabel('Gravimetric capacity (mAh/g)')
plt.tick_params(axis='both', which='both', direction='in', labelright=False, right=True, top=True)
plt.minorticks_on()
plt.legend(loc='lower right')


## Thickness vs capacity plot
thickCap = plt.figure(2)
x_lab = ['CO1 <1um', 'C6 3.7-4.8um', 'C7 8.2-11.5um']
x = np.arange(len(x_lab))
width = 0.2

cplot = [1, 10, 50]

barco1 = np.empty(shape=(len(cplot)), dtype=object)
barc6 = np.empty(shape=(len(cplot)), dtype=object)
barc7 = np.empty(shape=(len(cplot)), dtype=object)

co1min = np.empty(shape=(len(cplot)), dtype=object)
c6min = np.empty(shape=(len(cplot)), dtype=object)
c7min = np.empty(shape=(len(cplot)), dtype=object)

co1max = np.empty(shape=(len(cplot)), dtype=object)
c6max = np.empty(shape=(len(cplot)), dtype=object)
c7max = np.empty(shape=(len(cplot)), dtype=object)

for i in range(len(cplot)):
    barco1[i] = median([discharge[cplot[i], 4], discharge[cplot[i], 5]])
    barc6[i] = median([discharge[cplot[i], 0], discharge[cplot[i], 1]])
    barc7[i] = median([discharge[cplot[i], 2], discharge[cplot[i], 3]])

y = np.vstack((barco1, barc6, barc7))

for i in range(len(cplot)):
    co1min[i] = barco1[i]-min([discharge[cplot[i], 4], discharge[cplot[i], 5]])
    c6min[i] = barc6[i]-min([discharge[cplot[i], 0], discharge[cplot[i], 1]])
    c7min[i] = barc7[i]-min([discharge[cplot[i], 2], discharge[cplot[i], 3]])
    co1max[i] = max([discharge[cplot[i], 4], discharge[cplot[i], 5]])-barco1[i]
    c6max[i] = max([discharge[cplot[i], 0], discharge[cplot[i], 1]])-barc6[i]
    c7max[i] = max([discharge[cplot[i], 2], discharge[cplot[i], 3]])-barc7[i]

    errbarmin = np.vstack((co1min, c6min, c7min))
    errbarmax = np.vstack((co1max, c6max, c7max))
    
##cycle1 = plt.plot(x, y[0, :])
cycle1 = plt.errorbar(x_lab, y[0, :], xerr=None, yerr=errbarmin[:, 0], ls='none', marker='x', capsize=5, color='black', label='Cycle 1')
cycle10 = plt.errorbar(x_lab, y[1, :], xerr=None, yerr=errbarmin[:, 1], ls='none', marker='x', capsize=5, color='blue', label='Cycle 10')
cycle100 = plt.errorbar(x_lab, y[2, :], xerr=None, yerr=errbarmin[:, 2], ls='none', marker='x', capsize=5, color='red', label='Cycle 100')

minorLocator = AutoMinorLocator()
##plt.XAxis.set_minor_locator(minorLocator)

plt.xlabel('Hard carbon thickness')
plt.ylabel("Specific capacity (mAh/g)")
plt.tick_params(axis='y', which='both', direction='in', labelright=False, right=True)
plt.minorticks_on()
plt.tick_params(which='minor', direction='in', right=True, left=True)
plt.tick_params(axis='x', which='both', bottom=False)


plt.legend()


plt.show()





