import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pickle

# When copy-n-paste, think "function"
def loadData(filepath):

    with open(filepath, 'rb') as file:
        data = pickle.load(file)
        positions = data['positions']
        times = data['time']

        new_positions = np.nan * np.ones((len(positions), 50, 2))
        for i, c in enumerate(positions):
            for j, cc in enumerate(c):
                if cc[1] < 0 or cc[1] > 2.6:
                    new_positions[i, j, :] = [np.nan, np.nan]
                else:
                    new_positions[i, j, :] = cc

    return times, new_positions

#b100_pressure_start_idx = 300

prepend = 'E:/rec/2,5cm/1x/'
a100times, a100pos = loadData('{}1_before_pressure_increase_2,5cm_1x_Light0001.pickle'.format(prepend))
#a100starttime = a100times[a100_pressure_start_idx]
#plt.plot(a100times-a100starttime, np.nanmean(a100pos[:, :7, 1], axis=1))
#plt.show()
b100times, b100pos = loadData('{}2_pressure_increase_2,5cm_1x_Light0002.pickle'.format(prepend))
c100times, c100pos = loadData('{}3_after_pressure_increase_2,5cm_1x_Light0003.pickle'.format(prepend))
d100times, d100pos = loadData('{}4_pressure_decrease_2,5cm_1x_Light0004.pickle'.format(prepend))
e100times, e100pos = loadData('{}5_after_pressure_decrease_2,5cm_1x_Light0005.pickle'.format(prepend))

def normParams(values):
    return np.nanmean(values), np.nanstd(values)

a100_mean, a100_std = normParams(a100pos[5:3000, 0, 1])
b100_mean, b100_std = normParams(b100pos[5:3000, 0, 1])
c100_mean, c100_std = normParams(c100pos[5:3000, 0, 1])
d100_mean, d100_std = normParams(d100pos[5:3000, 0, 1])
e100_mean, e100_std = normParams(e100pos[5:3000, 0, 1])

Recordings = ['before pi', 'during pi', 'after pi', 'during pd', 'after pd']
count = np.arange(len(Recordings))

means = [a100_mean, b100_mean, c100_mean, d100_mean, e100_mean]
std = [a100_std, b100_std, c100_std, d100_std, e100_std]

fig, ax = plt.subplots()

ax.bar(count, means, yerr=std, align='center', alpha=0.5, ecolor='black', capsize=5)
ax.set_xticks(count)
ax.set_xticklabels(Recordings)
ax.yaxis.grid(True)
ax.set_ylabel('Distance from Water surface')
ax.set_xlabel('Phase')
ax.set_title('Swimmingheight in dependency of Pressure Change for 2,5cm Waterlevel')
ax.legend()

plt.tight_layout()
plt.show()