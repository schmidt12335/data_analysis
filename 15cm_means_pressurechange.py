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

prepend = 'E:/rec/15cm/1x/'
lowerbound, upperbound = 0, 12.8
a100times, a100pos = loadData('{}1_before_pressure_increase_15cm_1x_light.pickle'.format(prepend), lowerbound, upperbound)
b100times, b100pos = loadData('{}2_pressure_increase_15cm_1x_light.pickle'.format(prepend), lowerbound, upperbound)
c100times, c100pos = loadData('{}3_after_pressure_increase_15cm_1x_light.pickle'.format(prepend), lowerbound, upperbound)
d100times, d100pos = loadData('{}4_pressure_decrease_15cm_1x_light.pickle'.format(prepend),lowerbound, upperbound)
e100times, e100pos = loadData('{}5_after_pressure_decrease_15cm_1x_light.pickle'.format(prepend),lowerbound, upperbound)

def normParams(values):
    return np.nanmean(values), np.nanstd(values)


a100_mean, a100_std = normParams(a100pos[5:3000, :5, 1])
b100_mean, b100_std = normParams(b100pos[5:3000, 1:3, 1])
c100_mean, c100_std = normParams(c100pos[5:3000, :5, 1])
d100_mean, d100_std = normParams(d100pos[5:3000, :3, 1])
e100_mean, e100_std = normParams(e100pos[5:3000, :4, 1])

Recordings = ['before PI', 'during PI', 'after PI', 'during PD', 'after PD']
count = np.arange(len(Recordings))
means = [a100_mean, b100_mean, c100_mean, d100_mean, e100_mean]
std = [a100_std, b100_std, c100_std, d100_std, e100_std]

fig, ax = plt.subplots(figsize=(10,6))

ax.bar(count, means, width=0.5, edgecolor='black', yerr=std, alpha=0.5, ecolor='black', capsize=5)
ax.set_xticks(count)
ax.set_xticklabels(Recordings)
ax.yaxis.grid(True)
ax.set_ylabel('Distance from Water surface', fontsize=12)
ax.set_xlabel('Phase')
ax.set_title('Mean Swimmingheights during Pressure Change at 15cm Waterlevel')

ax.legend()

plt.tight_layout()
plt.show()

