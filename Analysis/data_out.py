import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pickle

filepath = 'E:/rec/swimheight/swimheight_light_10cm_Scale100pc.pickle'
with open(filepath,'rb') as file:
    data = pickle.load(file)
    positions = data['positions']
    times = data['time']

pos = np.nan * np.ones((len(positions),50,2))
for i, c in enumerate(positions):
    for j,cc in enumerate(c):
        pos[i,j,:] = cc

a = pos[:3000,0,1]
a = a[~np.isnan(a)]
np.mean(a)
print(np.mean(a))
