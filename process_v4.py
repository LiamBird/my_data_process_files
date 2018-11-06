## Processing capacity vs cycles data
## Scatter plot or column chart of gravimetric capacity output

## Importing libraries:
from csv import reader      # Data files are tab separated text files
import numpy
import numpy as np
from numpy import median
import decimal
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.tools as tls

mass = [1.8722, 1.2329, 1.8011, 3.6468]      #electrode material masses (mg)
massg = numpy.empty(len(mass), dtype=object) #set up array for masses in g
for m in range(len(mass)):                   #populate mass (g) array
    massg[m] = float(mass[m]/1000)

## Set up variables for read data to write to
##datac1oa = []
##datac1ob = []
datac6a = []
datac6b = []
datac7a = []
datac7b = []

## Open data files (.txt files) and append to variables above
with open('C6A_181102.txt', newline='') as fC6a:
    for row in reader(fC6a, delimiter='\t'):
        datac6a.append(row)

with open('C6B_181102.txt', newline='') as fC6b:
    for row in reader(fC6b, delimiter='\t'):
        datac6b.append(row)

with open('C7A_181102.txt', newline='') as fC7a:
    for row in reader(fC7a, delimiter='\t'):
        datac7a.append(row)

with open('C7B_181102.txt', newline='') as fC7b:
    for row in reader(fC7b, delimiter='\t'):
        datac7b.append(row)

## Deleting first rows (need to change 'open' commands in future versions)
c6a = np.delete(datac6a, (0), axis=0)
c6b = np.delete(datac6b, (0), axis=0)
c7a = np.delete(datac7a, (0), axis=0)
c7b = np.delete(datac7b, (0), axis=0)

## Set up array to contain data
data = np.array([c6a, c6b, c7a, c7b]) 
    
R = data.shape[0]   # number of rows in array
C = data.shape[1]   # number of columns in array
L = data.shape[2]   # number of layers in array (3D)

## Set up and populate array containing discharge capacities in mAh
## N.B.: capacities still str
discharge = numpy.empty(shape=(C, L), dtype=object)
discharge[:, 0] = data[[0], :, [2]]
discharge[:, 1] = data[[1], :, [2]]
discharge[:, 2] = data[[2], :, [2]]
discharge[:, 3] = data[[3], :, [2]]

## Parse str capacities to float
for i in range(C):
    for k in range(L):
        discharge[i, k] = float(discharge[i, k])

## Set up array to contain gravimetric capacities
dischargemAhg = numpy.empty(shape=(C,L), dtype=object)

## Set up array to count cycles (for abscissa)
cycles = numpy.empty(C, dtype=object)

## Calculate gravimetric capacities from capacities and count cycles
for i in range(C):
    for k in range(L):
        dischargemAhg[i, k] = round(discharge[i, k]/massg[m], 2)
        cycles[i] = i

dischargemAhg[0, 1] = dischargemAhg[1, 1]

## Making scatter plot
cap_cycles = plt.figure(2)
x = cycles
yc6a = dischargemAhg[:, 0]
yc6b = dischargemAhg[:, 1]
yc7a = dischargemAhg[:, 2]
yc7b = dischargemAhg[:, 3]
c6aplot = plt.plot(x,yc6a, 'o', label="C6")
c6bplot = plt.plot(x, yc6b, 'o', label="C6")
c7aplot = plt.plot(x,yc7a, 'o', label="C7")
c7bplot = plt.plot(x, yc7b, 'o', label="C7")
plt.xlim(0, 100)
plt.ylim(0, 400)
plt.legend()
plt.xlabel('Cycle number')
plt.ylabel('Gravimetric capacity (mAh/g)')

#### Initial capacity/ 10th cycle capacity bar plot
cycles_compare = plt.figure(1)

ci = 0
cn = 50

lab = [ci, cn]
barc6 = (median([dischargemAhg[ci, 0], dischargemAhg[ci, 1]]), median([dischargemAhg[cn, 0], dischargemAhg[cn, 1]]))
barc7 = (median([dischargemAhg[ci, 2], dischargemAhg[ci, 3]]), median([dischargemAhg[cn, 2], dischargemAhg[cn, 3]]))

x_lab = np.arange(len(lab))

plt.bar(x_lab - 0.2, barc6, 0.4, label='C6 3.7-4.8um')
plt.bar(x_lab + 0.2, barc7, 0.4, label='C7 8.2-11.5um')

plt.xticks(x_lab, lab)
plt.legend()
plt.xlabel('Cycle number')
plt.ylabel('Gravimetric capacity (mAh/g)')
plt.minorticks_on()
plt.grid(which="both", axis="y", linestyle="--")

plt.show()


