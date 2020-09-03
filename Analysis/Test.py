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

a_nan = pos[:3000, 0, 1]
a = [~np.isnan(a_nan)]
a_mean = np.mean(a)
a_std = np.std(a)
b_mean = 0.6
d_mean = 0.3

names = ['Fish_a','Fish_b','Fish_d']
values = [a_mean, b_mean, d_mean]
plt.bar(names, values)
plt.show()



#a = pos[:3000,0,1]
#plt.plot(times[:3000], a,'--',alpha = 0.4)
#plt.show()

