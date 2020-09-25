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
lowerbound, upperbound = 0, 2.6
a100times, a100pos = loadData('{}swimheight_light_2,5cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)
lowerbound, upperbound = 0, 5
b100times, b100pos = loadData('{}swimheight_light_5cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)
lowerbound, upperbound = 0, 10
c100times, c100pos = loadData('{}swimheight_light_10cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)
lowerbound, upperbound = 0, 12
d100times, d100pos = loadData('{}swimheight_light_15cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)

def normParams(values):
    return np.nanmedian(values), np.nanstd(values)

a100_mean, a100_std = normParams(a100pos[5:3000, :9, 1])
b100_mean, b100_std = normParams(b100pos[5:3000, :9, 1])
c100_mean, c100_std = normParams(c100pos[5:3000, (1,2,3,4), 1])
d100_mean, d100_std = normParams(d100pos[5:3000, :4, 1])

Recordings = ['2,5cm', '5cm', '10cm', '15cm']
count = np.arange(len(Recordings))

means = [a100_mean, b100_mean, c100_mean, d100_mean]
std = [a100_std, b100_std, c100_std, d100_std]

fig, ax = plt.subplots()

ax.bar(count, means, width=0.75, edgecolor='black', yerr=std, align='center', alpha=0.5, ecolor='black', capsize=5)
ax.set_xticks(count)
ax.set_xticklabels(Recordings)
ax.yaxis.grid(True)
ax.set_ylabel('Distance from Water surface')
ax.set_xlabel('Waterlevel')
ax.set_title('Swimmingheight in dependency of Waterlevel')
ax.legend()

plt.tight_layout()
plt.show()
