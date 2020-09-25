import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pickle

# When copy-n-paste, think "function"
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

prepend = 'E:/rec/swimheight_all/'
lowerbound, upperbound = 0, 12.8
a100times, a100pos = loadData('{}swimheight_light_10cm_Scale50pc.pickle'.format(prepend), lowerbound, upperbound)
lowerbound, upperbound = 0, 12.8
b100times, b100pos = loadData('{}swimheight_light_10cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)
lowerbound, upperbound = 0, 12.8
c100times, c100pos = loadData('{}swimheight_light_10cm_Scale150pc.pickle'.format(prepend), lowerbound, upperbound)


def normParams(values):
    return np.nanmean(values), np.nanstd(values)

a100_mean, a100_std = normParams(a100pos[5:3000, :9, 1])
b100_mean, b100_std = normParams(b100pos[5:3000, :4, 1])
c100_mean, c100_std = normParams(c100pos[5:3000, (0,1,2,3,6), 1])

Recordings = ['0,5x', '1x', '1,5x']
count = np.arange(len(Recordings))

means = [a100_mean, b100_mean, c100_mean]
std = [a100_std, b100_std, c100_std]

fig, ax = plt.subplots()

ax.bar(count, means, width=0.5, edgecolor='black', yerr=std, alpha=0.5, ecolor='black', capsize=5)
ax.set_xticks(count)
ax.set_xticklabels(Recordings)
ax.yaxis.grid(True)
ax.set_ylabel('Distance from Water surface')
ax.set_xlabel('Groundtexture scale')
ax.set_title('Swimmingheight in dependency of Groundtexture scaling at 10cm Waterlevel')
ax.legend()

plt.tight_layout()
plt.show()
