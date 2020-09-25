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
prepend = 'E:/rec/swimheight_all/'
lowerbound, upperbound = 0, 2.8
a50times, a50pos = loadData('{}swimheight_light_2,5cm_Scale50pc.pickle'.format(prepend), lowerbound, upperbound)
a100times, a100pos = loadData('{}swimheight_light_2,5cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)
a150times, a150pos = loadData('{}swimheight_light_2,5cm_Scale150pc.pickle'.format(prepend), lowerbound, upperbound)

#Data conversion Recording B
lowerbound, upperbound = 0, 5
b50times, b50pos = loadData('{}swimheight_light_5cm_Scale50pc.pickle'.format(prepend), lowerbound, upperbound)
b100times, b100pos = loadData('{}swimheight_light_5cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)
b150times, b150pos = loadData('{}swimheight_light_5cm_Scale150pc.pickle'.format(prepend), lowerbound, upperbound)

#Data conversion Recording C
lowerbound, upperbound = 0, 10
c50times, c50pos = loadData('{}swimheight_light_10cm_Scale50pc.pickle'.format(prepend), lowerbound, upperbound)
c100times, c100pos = loadData('{}swimheight_light_10cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)
c150times, c150pos = loadData('{}swimheight_light_10cm_Scale150pc.pickle'.format(prepend), lowerbound, upperbound)

#Data conversion Recording D
lowerbound, upperbound = 0, 12.8
d50times, d50pos = loadData('{}swimheight_light_15cm_Scale50pc.pickle'.format(prepend), lowerbound, upperbound)
d100times, d100pos = loadData('{}swimheight_light_15cm_Scale100pc.pickle'.format(prepend), lowerbound, upperbound)
d150times, d150pos = loadData('{}swimheight_light_15cm_Scale150pc.pickle'.format(prepend), lowerbound, upperbound)


#Deleting nan-values, calculating mean

def normParams(values):
    return np.nanmean(values), np.nanstd(values)  # nanmean/nanstd ignore NaNs by default


a50_mean, a50_std = normParams(a50pos[5:3000, :7, 1])
a100_mean, a100_std = normParams(a100pos[5:3000, :7, 1])
a150_mean, a150_std = normParams(a150pos[5:3000, :7, 1])

b50_mean, b50_std = normParams(b50pos[5:3000, (4,5,6), 1])
b100_mean, b100_std = normParams(b100pos[5:3000, :7, 1])
b150_mean, b150_std = normParams(b150pos[5:3000, (1,4,7,8,9), 1])

c50_mean, c50_std = normParams(c50pos[5:3000, :7, 1])
c100_mean, c100_std = normParams(c100pos[5:3000, :7, 1])
c150_mean, c150_std = normParams(c150pos[5:3000, :7, 1])

d50_mean, d50_std = normParams(d50pos[5:3000, :7, 1])
d100_mean, d100_std = normParams(d100pos[5:3000, :4, 1])
d150_mean, d150_std = normParams(d150pos[5:3000, :4, 1])

#Chart values

Recordings = ['2,5cm', '5cm', '10cm', '15cm']
count = np.arange(len(Recordings))

#sorting means

means = [a50_mean, a100_mean, a150_mean, b50_mean, b100_mean, b150_mean, c50_mean, c100_mean, c150_mean, d50_mean, d100_mean, d150_mean]
means50 = means[::3]
means100 = means[1::3]
means150 = means[2::3]

#sorting errors

std = [a50_std, a100_std, a150_std, b50_std, b100_std, b150_std, c50_std, c100_std, c150_std, d50_std, d100_std, d150_std]
error50 = std[::3]
error100 = std[1::3]
error150 = std[2::3]

width = 0.66

# names = ['Fish_a','Fish_b','Fish_d']
# values = [a,b,d]

fig, ax = plt.subplots()

rects1 = ax.bar(count - width/3, means50, width/3, yerr=error50, align='center', alpha=0.8, ecolor='blue', capsize=4, label='0,5x scaling')
rects2 = ax.bar(count, means100, width/3, yerr=error100, align='center', alpha=0.8, ecolor='red', capsize=4, label='1x scaling')
rects3 = ax.bar(count + width/3, means150, width/3, yerr=error150, align='center', alpha=0.8, ecolor='green', capsize=4, label='1,5x scaling')

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

plt.tight_layout()
plt.show()
