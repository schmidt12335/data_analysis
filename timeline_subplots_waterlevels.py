import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pickle

def loadData(filepath, lowerbound, upperbound):

    with open(filepath, 'rb') as file:
        data = pickle.load(file)
        positions = data['positions']
        times = data['time']

        new_positions = np.nan * np.ones((len(positions), 50, 2))
        for i, c in enumerate(positions):
            for j, cc in enumerate(c):
                if cc[1] < lowerbound or cc[1] > upperbound:
                    new_positions[i, j, :] = [np.nan, np.nan]
                else:
                    new_positions[i, j, :] = cc

    return times, new_positions

#Data conversion Recording A
prepend = 'E:/rec/swimheight_all/'
lowerbound, upperbound = 0, 2.8
atimes, apos = loadData('{}swimheight_light_2,5cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)
lowerbound, upperbound = 0, 5
btimes, bpos = loadData('{}swimheight_light_5cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)
lowerbound, upperbound = 0, 5
ctimes, cpos = loadData('{}swimheight_light_10cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)
lowerbound, upperbound = 0, 5
dtimes, dpos = loadData('{}swimheight_light_15cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)

a = apos[5:3000, 0, 1]
at = atimes[5:3000]
b = bpos[5:3000, 1, 1]
bt = btimes[5:3000]
c = cpos[5:3000, 0, 1]
ct =ctimes[5:3000]
d = dpos[5:3000, 0, 1]
dt = dtimes[5:3000]

f, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharey=True, sharex=True, figsize=(12, 8))

ax1.plot(at-at[0],a)
ax1.set_title('2,5cm')
ax2.plot(bt-bt[0], b)
ax2.set_title('5cm')
ax3.plot(ct-ct[0], c)
ax3.set_title('10cm')
ax4.plot(dt-dt[0], d)
ax4.set_title('15cm')
ax4.set_xlabel('Time in Frames (5 Frames equals 1 Second)', fontsize='large')
f.suptitle('Example Fish of different Waterlevels')
f.text(0.08,0.325,'Distance from Watersurface (cm)', rotation='vertical', fontsize='large')

plt.show()
