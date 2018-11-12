## Processing cell potential data

## Importing libraries:
from csv import reader
import numpy as np
import decimal
import matplotlib.pyplot as plt

## Set up variables for read data to write to
c6Araw = []

## Open data files (.txt file) and append to variables above
c6Afile = '6A_capvolt.txt'
with open('6A_capvolt.txt', newline = '') as dC6a:
    for row in reader(dC6a, delimiter='\t'):
        c6Araw.append(row)


c6ahead = np.asarray(c6Araw)

for i in range(len(c6ahead)):
    if c6ahead[i] == ['Voltage/V', 'Capacity/mAh']:
        header = i

c6alst = np.delete(c6ahead,np.s_[0:header+1], axis=0)

c6a = np.empty(shape=(len(c6alst), 2), dtype=object)

c6a[0, 0] = float(c6alst[0][0])
c6a[0, 1] = float(c6alst[0][1])

for i in range(len(c6alst)-2):
    c6a[i, 0] = float(c6alst[i][0])
    c6a[i, 1] = float(c6alst[i][1])

v = c6a[:, 0]
c = c6a[:, 1]

bp = []
for i in range(1,len(c)-1):
    if c[i]==0 and c[i+1]>0:
        bp.append(i)

## Need to adapt this to make a loop to compare next cycle duration with current maximum matrix size, pad as required
        
Ccycle = c[bp[0]:bp[1]]
Vcycle = v[bp[0]:bp[1]]
cycle = np.vstack((Ccycle, Vcycle))

Ccycle1 = c[bp[1]:bp[2]]
Vcycle1 = v[bp[1]:bp[2]]
cycle1 = np.vstack((Ccycle1, Vcycle1))

ml = max(cycle.shape[1], cycle1.shape[1])

cycle = np.pad(cycle, ((0, 0), (ml-cycle.shape[1], 0)), 'constant', constant_values=(0, 0))

cycleStack = np.dstack((cycle, cycle1))

## Making plot
dx1 = cycleStack[0, :, 0]
dy1 = cycleStack[1, :, 0]

dx2 = cycleStack[0, :, 1]
dy2 = cycleStack[1, :, 1]

gr1 = plt.plot(dx1, dy1, label='1st Disch')
gr2 = plt.plot(dx2, dy2, label='1st Ch')
plt.legend()

plt.show()

