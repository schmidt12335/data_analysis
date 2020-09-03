import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pickle

#Data conversion Recording A

afilepath = 'E:/rec/swimheight_all/swimheight_light_2,5cm_Scale100pc.pickle'
with open(afilepath, 'rb') as file:
    adata = pickle.load(file)
    apositions = adata['positions']
    atimes = adata['time']

apos = np.nan * np.ones((len(apositions), 50, 2))
for i, c in enumerate(apositions):
    for j, cc in enumerate(c):
        apos[i, j, :] = cc
#Data conversion Recording D

dfilepath = 'E:/rec/swimheight_all/swimheight_light_2,5cm_Scale100pc.pickle'
with open(dfilepath, 'rb') as file:
    ddata = pickle.load(file)
    dpositions = ddata['positions']
    dtimes = ddata['time']

dpos = np.nan * np.ones((len(dpositions), 50, 2))
for i, c in enumerate(dpositions):
    for j, cc in enumerate(c):
        dpos[i, j, :] = cc

#Data conversion Recording B

bfilepath = 'E:/rec/swimheight_all/swimheight_light_5cm_Scale100pc.pickle'
with open(bfilepath, 'rb') as file:
    bdata = pickle.load(file)
    bpositions = bdata['positions']
    btimes = bdata['time']

bpos = np.nan * np.ones((len(bpositions), 50, 2))
for i, c in enumerate(bpositions):
    for j, cc in enumerate(c):
        bpos[i, j, :] = cc

#Data conversion Recording C

cfilepath = 'E:/rec/swimheight_all/swimheight_light_10cm_Scale100pc.pickle'
with open(cfilepath, 'rb') as file:
    cdata = pickle.load(file)
    cpositions = cdata['positions']
    ctimes = cdata['time']

cpos = np.nan * np.ones((len(cpositions), 50, 2))
for i, c in enumerate(cpositions):
    for j, cc in enumerate(c):
        cpos[i, j, :] = cc

#Data conversion Recording D

dfilepath = 'E:/rec/swimheight_all/swimheight_light_15cm_Scale100pc.pickle'
with open(dfilepath, 'rb') as file:
    ddata = pickle.load(file)
    dpositions = ddata['positions']
    dtimes = ddata['time']

dpos = np.nan * np.ones((len(dpositions), 50, 2))
for i, c in enumerate(dpositions):
    for j, cc in enumerate(c):
        dpos[i, j, :] = cc

#Deleting nan-values, calculating mean
a_nan = apos[5:3000, 0, 1]
a = a_nan[~np.isnan(a_nan)]
a_mean = np.mean(a)
a_std = np.std(a)

b_nan = bpos[5:3000, 0, 1]
b = b_nan[~np.isnan(b_nan)]
b_mean = np.mean(b)
b_std = np.std(b)

c_nan = cpos[5:3000, 0, 1]
c = c_nan[~np.isnan(c_nan)]
c_mean = np.mean(c)
c_std = np.std(c)

d_nan = dpos[5:3000, 0, 1]
d = d_nan[~np.isnan(d_nan)]
d_mean = np.mean(d)
d_std = np.std(d)

#Chart values

Recordings = ['2,5cm','5cm', '10cm', '15cm']
count = np.arange(len(Recordings))
means = [a_mean, b_mean, c_mean, d_mean]
error = [a_std, b_std, c_std, d_std]
# names = ['Fish_a','Fish_b','Fish_d']
# values = [a,b,d]

fig, ax = plt.subplots()
ax.bar(count, means, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=5)
ax.set_xticks(count)
ax.set_xticklabels(Recordings)
ax.yaxis.grid(True)
ax.set_ylabel('Distance from Water surface')
ax.set_xlabel('Waterlevel')
ax.set_title('Swimmingheight in dependency of Waterlevel')
plt.tight_layout()
plt.show()
