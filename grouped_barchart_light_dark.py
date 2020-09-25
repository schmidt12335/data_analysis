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


# Data conversion Recording A
prepend = 'E:/rec/swimheight_all/'
lowerbound, upperbound = 0, 2.8
a100times, a100pos = loadData('{}swimheight_light_2,5cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)
a100timesdark, a100posdark = loadData('{}swimheight_dark_2,5cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)

# Data conversion Recording B
lowerbound, upperbound = 0, 5
b100times, b100pos = loadData('{}swimheight_light_5cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)
b100timesdark, b100posdark = loadData('{}swimheight_dark_5cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)

# Data conversion Recording C
lowerbound, upperbound = 0, 10
c100times, c100pos = loadData('{}swimheight_light_10cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)
c100timesdark, c100posdark = loadData('{}swimheight_dark_10cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)

# Data conversion Recording D
lowerbound, upperbound = 0, 11.1
d100times, d100pos = loadData('{}swimheight_light_15cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)
d100timesdark, d100posdark = loadData('{}swimheight_dark_15cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)


# Deleting nan-values, calculating mean

def normParams(values):
    return np.nanmedian(values), np.nanstd(values)  # nanmean/nanstd ignore NaNs by default


a100_mean, a100_std = normParams(a100pos[5:3000, :7, 1])
a100dark_mean, a100dark_std = normParams(a100posdark[5:3000, :7, 1])

b100_mean, b100_std = normParams(b100pos[5:3000, :7, 1])
b100dark_mean, b100dark_std = normParams(b100posdark[5:3000, :7, 1])

c100_mean, c100_std = normParams(c100pos[5:3000, (0,1,2,3,4), 1])
c100dark_mean, c100dark_std = normParams(c100posdark[5:3000, (1,5,6,7), 1])

d100_mean, d100_std = normParams(d100pos[5:3000, (0,1,2,3), 1])
d100dark_mean, d100dark_std = normParams(d100posdark[5:3000, (0,1,2,3,4,5), 1])

# Chart values

Recordings = ['2,5cm', '5cm', '10cm', '15cm']
count = np.arange(len(Recordings))

# sorting means

means = [a100_mean, a100dark_mean, b100_mean, b100dark_mean, c100_mean, c100dark_mean, d100_mean, d100dark_mean]

means100 = means[0::2]
means100_dark = means[1::2]

# sorting errors

std = [a100_std, a100dark_std, b100_std, b100dark_std, c100_std, c100dark_std, d100_std, d100dark_std]

error100 = std[0::2]
error100_dark = std[1::2]

width = 0.35

fig, ax = plt.subplots()

rects1 = ax.bar(count, means100, width, yerr=error100, align='center', alpha=0.8, ecolor='red', capsize=4, label='Light')
rects2 = ax.bar(count + width, means100_dark, width, yerr=error100_dark, align='center', alpha=0.8, ecolor='green', capsize=4, label='Dark')

# Plotting Axes

# ax.bar(count, means, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=5)
ax.set_xticks(count)
ax.set_xticklabels(Recordings)
ax.yaxis.grid(True)
ax.set_ylabel('Distance from Water surface')
ax.set_xlabel('Waterlevel')
ax.set_title('Swimmingheight during Light and Darkness')
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{:.2f}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 10),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.show()
