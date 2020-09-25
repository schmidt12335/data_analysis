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

#Data conversion Recording A
prepend = 'E:/rec/pressurechange_all/'
lowerbound, upperbound = 0, 2.8
a50times, a50pos = loadData('{}1_before_pressure_increase_2,5cm_1x_Light.pickle'.format(prepend), lowerbound, upperbound)
a100times, a100pos = loadData('{}2_pressure_increase_2,5cm_1x_Light.pickle'.format(prepend), lowerbound, upperbound)
a150times, a150pos = loadData('{}3_after_pressure_increase_2,5cm_1x_Light.pickle'.format(prepend), lowerbound, upperbound)
a200times, a200pos = loadData('{}4_pressure_decrease_2,5cm_1x_Light.pickle'.format(prepend), lowerbound, upperbound)
a250times, a250pos = loadData('{}5_after_pressure_decrease_2,5cm_1x_Light.pickle'.format(prepend), lowerbound, upperbound)

#Data conversion Recording B
lowerbound, upperbound = 0, 5
b50times, b50pos = loadData('{}1_before_pressure_increase_5cm_1x_Light.pickle'.format(prepend), lowerbound, upperbound)
b100times, b100pos = loadData('{}2_pressure_increase_5cm_1x_Light.pickle'.format(prepend), lowerbound, upperbound)
b150times, b150pos = loadData('{}3_after_pressure_increase_5cm_1x_light.pickle'.format(prepend), lowerbound, upperbound)
b200times, b200pos = loadData('{}4_pressure_decrease_5cm_1x_Light.pickle'.format(prepend), lowerbound, upperbound)
b250times, b250pos = loadData('{}5_after_pressure_decrease_5cm_1x_Light.pickle'.format(prepend), lowerbound, upperbound)

#Data conversion Recording C
lowerbound, upperbound = 0, 10
c50times, c50pos = loadData('{}1_before_pressure_increase_10cm_1x_light.pickle'.format(prepend), lowerbound, upperbound)
c100times, c100pos = loadData('{}2_pressure_increase_10cm_1x_light.pickle'.format(prepend), lowerbound, upperbound)
c150times, c150pos = loadData('{}3_after_pressure_increase_10cm_1x_light.pickle'.format(prepend), lowerbound, upperbound)
c200times, c200pos = loadData('{}4_pressure_decrease_10cm_1x_Light.pickle'.format(prepend), lowerbound, upperbound)
c250times, c250pos = loadData('{}5_after_pressure_decrease_10cm_1x_Light.pickle'.format(prepend), lowerbound, upperbound)

#Data conversion Recording D
lowerbound, upperbound = 0, 11.6
d50times, d50pos = loadData('{}1_before_pressure_increase_15cm_1x_light.pickle'.format(prepend), lowerbound, upperbound)
d100times, d100pos = loadData('{}2_pressure_increase_15cm_1x_light.pickle'.format(prepend), lowerbound, upperbound)
d150times, d150pos = loadData('{}3_after_pressure_increase_15cm_1x_light.pickle'.format(prepend), lowerbound, upperbound)
d200times, d200pos = loadData('{}4_pressure_decrease_15cm_1x_Light.pickle'.format(prepend), lowerbound, upperbound)
d250times, d250pos = loadData('{}5_after_pressure_decrease_15cm_1x_Light.pickle'.format(prepend), lowerbound, upperbound)

#Deleting nan-values, calculating mean

def normParams(values):
    return np.nanmedian(values), np.nanstd(values)  # nanmean/nanstd ignore NaNs by default


a50_mean, a50_std = normParams(a50pos[5:3000, :9, 1])
a100_mean, a100_std = normParams(a100pos[5:3000, :9, 1])
a150_mean, a150_std = normParams(a150pos[5:3000, :9, 1])
a200_mean, a200_std = normParams(a200pos[5:3000, :9, 1])
a250_mean, a250_std = normParams(a250pos[5:3000, :9, 1])

b50_mean, b50_std = normParams(b50pos[5:3000, :9, 1])
b100_mean, b100_std = normParams(b100pos[5:3000, :9, 1])
b150_mean, b150_std = normParams(b150pos[5:3000, :9, 1])
b200_mean, b200_std = normParams(b200pos[5:3000, :9, 1])
b250_mean, b250_std = normParams(b250pos[5:3000, :9, 1])

c50_mean, c50_std = normParams(c50pos[5:3000, :9, 1])
c100_mean, c100_std = normParams(c100pos[5:3000, :9, 1])
c150_mean, c150_std = normParams(c150pos[5:3000, :9, 1])
c200_mean, c200_std = normParams(c200pos[5:3000, :9, 1])
c250_mean, c250_std = normParams(c250pos[5:3000, :9, 1])

d50_mean, d50_std = normParams(d50pos[5:3000, :5, 1])
d100_mean, d100_std = normParams(d100pos[5:3000, 1:3, 1])
d150_mean, d150_std = normParams(d150pos[5:3000, :5, 1])
d200_mean, d200_std = normParams(d200pos[5:3000, :3, 1])
d250_mean, d250_std = normParams(d250pos[5:3000, :4, 1])

#Chart values

Recordings = ['before PI', 'during PI', 'after PI', 'during PD', 'after PD']
count = np.arange(len(Recordings))

#sorting means

means = [a50_mean, a100_mean, a150_mean, a200_mean, a250_mean, b50_mean, b100_mean, b150_mean, b200_mean, b250_mean, c50_mean, c100_mean, c150_mean, c200_mean, c250_mean, d50_mean, d100_mean, d150_mean, d200_mean, d250_mean]
means50 = means[::5]
means100 = means[1::5]
means150 = means[2::5]
means200 = means[3::5]
means300 = means[4::5]

#sorting errors

std = [a50_std, a100_std, a150_std, a200_std, a250_std, b50_std, b100_std, b150_std, b200_std, b250_std, c50_std, c100_std, c150_std, c200_std, c250_std, d50_std, d100_std, d150_std, d200_std, d250_std,]
error50 = std[::5]
error100 = std[1::5]
error150 = std[2::5]
error200 = std[3::5]
error250 = std[4::5]
width = 0.66

fig, ax = plt.subplots()

rects1 = ax.bar(count - width/5, means50, width/3, yerr=error50, align='center', alpha=0.8, ecolor='blue', capsize=4, label='before PI')
rects2 = ax.bar(count - width/5, means100, width/3, yerr=error100, align='center', alpha=0.8, ecolor='red', capsize=4, label='during PI')
rects3 = ax.bar(count, means150, width/3, yerr=error150, align='center', alpha=0.8, ecolor='green', capsize=4, label='after PI')
rects4 = ax.bar(count + width/5, means200, width/3, yerr=error200, align='center', alpha=0.8, ecolor='orange', capsize=4, label='before PD')
rects5 = ax.bar(count + width/5, means250, width/3, yerr=error250, align='center', alpha=0.8, ecolor='purple', capsize=4, label='after PD')

ax.set_xticks(count)
ax.set_xticklabels(Recordings)
ax.yaxis.grid(True)
ax.set_ylabel('Distance from Water surface')
ax.set_xlabel('Waterlevel')
ax.set_title('Swimmingheight in dependency of Waterlevel and Groundtexture scaling')
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
autolabel(rects3)
autolabel(rects4)
autolabel(rects5)

plt.tight_layout()
plt.show()