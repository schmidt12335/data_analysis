import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pickle

filepath = 'E:/rec/swimheight_all/swimheight_light_5cm_Scale50pc.pickle'
with open(filepath,'rb') as file:
    data = pickle.load(file)
    positions = data['positions']
    times = data['time']

pos = np.nan * np.ones((len(positions), 50, 2))
for i, c in enumerate(positions):
    for j, cc in enumerate(c):
        if cc[1] < 0 or cc[1] > 5:
            pos[i, j, :] = [np.nan, np.nan]
        else:
            pos[i, j, :] = cc
#import IPython
#IPython.embed()


fish0 = pos[5:3000, 0, 1]
fish1 = pos[5:3000, 1, 1]
fish2 = pos[5:3000, 2, 1]
fish3 = pos[5:3000, 3, 1]
fish4 = pos[5:3000, 4, 1]
fish5 = pos[5:3000, 5, 1]
fish6 = pos[5:3000, 6, 1]
fish7 = pos[5:3000, 7, 1]

mean_fish0 = np.mean(fish0[~np.isnan(fish0)])
mean_fish1 = np.mean(fish1[~np.isnan(fish1)])
mean_fish2 = np.mean(fish2[~np.isnan(fish2)])
mean_fish3 = np.mean(fish3[~np.isnan(fish3)])
mean_fish4 = np.mean(fish4[~np.isnan(fish4)])
mean_fish5 = np.mean(fish5[~np.isnan(fish5)])
mean_fish6 = np.mean(fish6[~np.isnan(fish6)])
mean_fish7 = np.mean(fish7[~np.isnan(fish7)])

means = [mean_fish0, mean_fish1, mean_fish2, mean_fish3, mean_fish4, mean_fish5, mean_fish6, mean_fish7]
mean_total = np.mean(means)
std = np.std(means)

names = ['fish1', 'fish2', 'fish3', 'fish4', 'fish5', 'fish6', 'fish7', 'fish8']
error = [0.2, 0.1, 0.2]
b_mean = 0.6
d_mean = 0.3
count = np.arange(len(names))

#append positions/means to one array -> mean and std ## arange

plt.bar(names, means)
plt.show()


#fig = plt.figure()
#for i in range(3):
#    plt.plot(times[5:3000], a[5:3000, 1], '--', alpha=0.4)
#plt.show()