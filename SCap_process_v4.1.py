import os
import glob
import pandas as pd
import numpy as np
from numpy import median

## Importing all text files from directory defined by path
##path = r'C:\Users\laure\OneDrive - University Of Cambridge\DATA\(0-0-1)(0-20)T\SCap'
##path = r'C:\Users\laure\OneDrive - University Of Cambridge\DATA\(0-0-1)(0-0)cP'
##path = r'C:\Users\laure\Dropbox\DATA\SCap\(0-0-1)(0-10)T'
##path = r'C:\Users\laure\Dropbox\DATA\SCap\(0-0-1)(0-0).P'
##path = r'C:\Users\laure\Dropbox\DATA\SCap\(0-0-1)(0-10)T'
##path = r'C:\Users\laure\Dropbox\DATA\SCap\(0-0-1)(0-20)T'
##path = r'C:\Users\laure\Dropbox\DATA\SCap\(0-0-1)(10-0)P'
path = r'C:\Users\laure\Dropbox\DATA\SCap\(0-0-1)(10-0)T'

allfiles = glob.glob(os.path.join(path, "*.txt"))
data_imp = (pd.read_csv(f, delimiter='\t', header='infer') for f in allfiles)
rawimp = np.asarray(pd.concat(data_imp))

## Identifying the lengths of each sample set
sl = []                             # Initialise variable for sample length
for i in range(len(rawimp)):        
    if rawimp[i, 0]==1:             # Look for cycle number 1 (in 0th column)
        sl.append(i)                # Record row numbers of new cycles ending

sl.append(len(rawimp))              # Append total length of rawimp data set

sle = np.zeros(shape=(len(sl)-1), dtype=int)        # Initialise variable for storing row ranges for each sample
for i in range(len(sl)-1):                          
    sle[i] = sl[i+1]-sl[i]                          # Subtract sample ends from sl to obtain lengths of sample data sets

data = np.empty(shape=(max(sle),        # Initialise empty numpy array with enough rows for the sample with the most rows...
                       4,               # 4 columns (all samples have Cycle, Charge, Discharge, Efficiency by default)...
                       len(sle)),       # enough layers for each sample (corresponds to number of values in sle)
                dtype=object)
discharge = np.empty(shape=(max(sle),
                            len(sle)),
                     dtype=float)


for i in range(len(sle)):
    data[range(sle[i]), :, i] = rawimp[range(sl[i], sl[i+1]), :]

for i in range(max(sle)):
    for j in range(len(sle)):
        discharge[i, j] = data[i, 2, j]

caprem = np.empty(shape=(discharge.shape[0],
                         discharge.shape[1]),
                  dtype=float)

for i in range(1, len(discharge)):
    for j in range(discharge.shape[1]):
        caprem[i, j] = (discharge[i, j]/discharge[1, j])*100



##filename = path+r'\processed\collected_data'
##open(filename, mode='wb')
##np.savetxt(filename+'.txt', discharge, fmt='%f', delimiter='\t', header='\n', footer='', comments='', encoding=None)
##np.save(filename, discharge)

filename_rem = path+r'\processed\caprem'
filename_abs = path+r'\processed\SCap'
open(filename_rem, mode = 'wb')
open(filename_abs, mode = 'wb')
np.savetxt(filename_rem+'.txt', caprem, fmt='%f', delimiter='\t', header='\n', footer = '', comments='', encoding=None)
np.savetxt(filename_abs+'.txt', discharge, fmt='%f', delimiter='\t', header='\n', footer = '', comments='', encoding=None)
np.save(filename_rem, caprem)
np.save(filename_abs, discharge)
