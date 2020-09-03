import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pickle

filepath = 'E:/rec/swimheight/swimheight_light_10cm_Scale100pc.pickle'
with open(filepath,'rb') as file:
    data = pickle.load(file)
    positions = data['positions']
    times = data['time']

max = 5
min = -0.5

pos = np.nan * np.ones((len(positions),50,2))
for i, c in enumerate(positions):
    for j,cc in enumerate(c):
        pos[i,j,:] = cc
    for j in range(-0.5,5):
        j = j-1
fig = plt.figure()
for i in range(2):
    plt.plot(times[5:3000], pos[5:3000, :-5, 1], '--', alpha=0.4)
plt.show()