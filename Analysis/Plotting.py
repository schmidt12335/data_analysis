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


print(pos)

nnan = pos[5:3000, 0, 1]
nan = nnan[~np.isnan(nnan)]

#fig = plt.figure()
#ax = fig.add_subplot(331,projection='3d')
#for i in range(3):
#   ax.plot(times[::10],pos[:,i,0][::10],pos[:,i,1][::10],'--',alpha=0.3)
#plt.show()

fig = plt.figure()
for i in range(2):
    plt.plot(times[5:3000], pos[5:3000, :-5, 1], '--', alpha=0.4)
plt.show()