from csv import reader
import numpy
import numpy as np
import decimal
import matplotlib.pyplot as plt

mass = [1.8722, 1.2329, 1.8011, 3.6468]      #mg
massg = numpy.empty(len(mass), dtype=object)
for m in range(len(mass)):
    massg[m] = float(mass[m]/1000)

datac6a = []
datac6b = []
datac7a = []
datac7b = []


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

c6a = np.delete(datac6a, (0), axis=0)
c6b = np.delete(datac6b, (0), axis=0)
c7a = np.delete(datac7a, (0), axis=0)
c7b = np.delete(datac7b, (0), axis=0)

data = np.array([c6a, c6b, c7a, c7b]) 
    
R = data.shape[0]
C = data.shape[1]
L = data.shape[2] 

discharge = numpy.empty(shape=(C, L), dtype=object)
discharge[:, 0] = data[[0], :, [2]]
discharge[:, 1] = data[[1], :, [2]]
discharge[:, 2] = data[[2], :, [2]]
discharge[:, 3] = data[[3], :, [2]]

for i in range(C):
    for k in range(L):
        discharge[i, k] = float(discharge[i, k])

dischargemAhg = numpy.empty(shape=(C,L), dtype=object)
cycles = numpy.empty(C, dtype=object)

for i in range(C):
    for k in range(L):
        dischargemAhg[i, k] = round(discharge[i, k]/massg[m], 2)
        cycles[i] = i

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
plt.show()
