import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pickle

#Data conversion Recording A

a50filepath = 'E:/rec/swimheight_all/swimheight_light_2,5cm_Scale100pc.pickle'
with open(a50filepath, 'rb') as file:
    a50data = pickle.load(file)
    a50positions = a50data['positions']
    a50times = a50data['time']

a50pos = np.nan * np.ones((len(a50positions), 50, 2))
for i, c in enumerate(a50positions):
    for j, cc in enumerate(c):
        if cc[1]<0 or cc[1]>2,8:
            a50pos[i,j,:] = [np.nan, np.nan]
        else:
            a50pos[i, j, :] = cc

a100filepath = 'E:/rec/swimheight_all/swimheight_light_2,5cm_Scale100pc.pickle'
with open(a100filepath, 'rb') as file:
    a100data = pickle.load(file)
    a100positions = a100data['positions']
    a100times = a100data['time']

a100pos = np.nan * np.ones((len(a100positions), 50, 2))
for i, c in enumerate(a100positions):
    for j, cc in enumerate(c):
        if cc[1]<0 or cc[1]>2,8:
            a100pos[i,j,:] = [np.nan, np.nan]
        else:
            a100pos[i, j, :] = cc

a150filepath = 'E:/rec/swimheight_all/swimheight_light_2,5cm_Scale100pc.pickle'
with open(a150filepath, 'rb') as file:
    a150data = pickle.load(file)
    a150positions = a150data['positions']
    a150times = a150data['time']

a150pos = np.nan * np.ones((len(a150positions), 50, 2))
for i, c in enumerate(a150positions):
    for j, cc in enumerate(c):
        if cc[1]<0 or cc[1]>2,8:
            a150pos[i,j,:] = [np.nan, np.nan]
        else:
            a150pos[i, j, :] = cc

#Data conversion Recording B

b50filepath = 'E:/rec/swimheight_all/swimheight_light_5cm_Scale50pc.pickle'
with open(b50filepath, 'rb') as file:
    b50data = pickle.load(file)
    b50positions = b50data['positions']
    b50times = b50data['time']

b50pos = np.nan * np.ones((len(b50positions), 50, 2))
for i, c in enumerate(b50positions):
    for j, cc in enumerate(c):
        if cc[1]<0 or cc[1]>2:
            b50pos[i,j,:] = [np.nan, np.nan]
        else:
            b50pos[i, j, :] = cc

b100filepath = 'E:/rec/swimheight_all/swimheight_light_5cm_Scale100pc.pickle'
with open(b100filepath, 'rb') as file:
    b100data = pickle.load(file)
    b100positions = a100data['positions']
    b100times = b100data['time']

b100pos = np.nan * np.ones((len(b100positions), 50, 2))
for i, c in enumerate(b100positions):
    for j, cc in enumerate(c):
        if cc[1]<0 or cc[1]>5:
            b100pos[i,j,:] = [np.nan, np.nan]
        else:
            b100pos[i, j, :] = cc

b150filepath = 'E:/rec/swimheight_all/swimheight_light_5cm_Scale100pc.pickle'
with open(b150filepath, 'rb') as file:
    b150data = pickle.load(file)
    b150positions = a150data['positions']
    b150times = a150data['time']

b150pos = np.nan * np.ones((len(b150positions), 50, 2))
for i, c in enumerate(b150positions):
    for j, cc in enumerate(c):
        if cc[1]<0 or cc[1]>5:
            b150pos[i,j,:] = [np.nan, np.nan]
        else:
            b150pos[i, j, :] = cc

#Data conversion Recording C

c50filepath = 'E:/rec/swimheight_all/swimheight_light_10cm_Scale50pc.pickle'
with open(c50filepath, 'rb') as file:
    c50data = pickle.load(file)
    c50positions = c50data['positions']
    c50times = c50data['time']

c50pos = np.nan * np.ones((len(c50positions), 50, 2))
for i, c in enumerate(c50positions):
    for j, cc in enumerate(c):
        if cc[1]<0 or cc[1]>10:
            c50pos[i,j,:] = [np.nan, np.nan]
        else:
            c50pos[i, j, :] = cc

c100filepath = 'E:/rec/swimheight_all/swimheight_light_10cm_Scale100pc.pickle'
with open(c100filepath, 'rb') as file:
    c100data = pickle.load(file)
    c100positions = c100data['positions']
    c100times = c100data['time']

c100pos = np.nan * np.ones((len(c100positions), 50, 2))
for i, c in enumerate(c100positions):
    for j, cc in enumerate(c):
        if cc[1]<0 or cc[1]>10:
            c100pos[i,j,:] = [np.nan, np.nan]
        else:
            c100pos[i, j, :] = cc

c150filepath = 'E:/rec/swimheight_all/swimheight_light_10cm_Scale150pc.pickle'
with open(c150filepath, 'rb') as file:
    c150data = pickle.load(file)
    c150positions = c150data['positions']
    c150times = c150data['time']

c150pos = np.nan * np.ones((len(c150positions), 50, 2))
for i, c in enumerate(c150positions):
    for j, cc in enumerate(c):
        if cc[1]<0 or cc[1]>10:
            c150pos[i,j,:] = [np.nan, np.nan]
        else:
            c150pos[i, j, :] = cc

#plt.plot(ctimes[5:3000], cpos[5:3000,:, 1], '--', alpha=0.4)
#plt.show()
#Data conversion Recording D

d50filepath = 'E:/rec/swimheight_all/swimheight_light_15cm_Scale50pc.pickle'
with open(d50filepath, 'rb') as file:
    d50data = pickle.load(file)
    d50positions = d50data['positions']
    d50times = d50data['time']

d50pos = np.nan * np.ones((len(d50positions), 50, 2))
for i, c in enumerate(d50positions):
    for j, cc in enumerate(c):
        if cc[1]<0 or cc[1]>15:
            d50pos[i,j,:] = [np.nan, np.nan]
        else:
            d50pos[i, j, :] = cc

d100filepath = 'E:/rec/swimheight_all/swimheight_light_15cm_Scale100pc.pickle'
with open(d100filepath, 'rb') as file:
    d100data = pickle.load(file)
    d100positions = d100data['positions']
    d100times = d100data['time']

d100pos = np.nan * np.ones((len(d100positions), 50, 2))
for i, c in enumerate(d100positions):
    for j, cc in enumerate(c):
        if cc[1]<0 or cc[1]>15:
            d100pos[i,j,:] = [np.nan, np.nan]
        else:
            d100pos[i, j, :] = cc

d150filepath = 'E:/rec/swimheight_all/swimheight_light_15cm_Scale100pc.pickle'
with open(d150filepath, 'rb') as file:
    d150data = pickle.load(file)
    d150positions = d150data['positions']
    d150times = d150data['time']

d150pos = np.nan * np.ones((len(d150positions), 50, 2))
for i, c in enumerate(d150positions):
    for j, cc in enumerate(c):
        if cc[1]<0 or cc[1]>15:
            d150pos[i,j,:] = [np.nan, np.nan]
        else:
            d150pos[i, j, :] = cc

#Deleting nan-values, calculating mean

fish1 = pos[5:3000, 0, 1]
mean_fish1 = np.mean(fish1)
fish1_std = np.std(fish1)

a50_nan = a50pos[5:3000, :, 1]
a50 = a50_nan[~np.isnan(a50_nan)]
a50_mean = np.mean(a50)
a50_std = np.std(a50)

a100_nan = a100pos[5:3000, 0, 1]
a100 = a100_nan[~np.isnan(a100_nan)]
a100_mean = np.mean(a100)
a100_std = np.std(a100)

a150_nan = a150pos[5:3000, 0, 1]
a150 = a150_nan[~np.isnan(a150_nan)]
a150_mean = np.mean(a150)
a150_std = np.std(a150)

b50_nan = b50pos[5:3000, 0, 1]
b50 = b50_nan[~np.isnan(b50_nan)]
b50_mean = np.mean(b50)
b50_std = np.std(b50)

b100_nan = b100pos[5:3000, 0, 1]
b100 = b100_nan[~np.isnan(b100_nan)]
b100_mean = np.mean(b100)
b100_std = np.std(b100)

b150_nan = b150pos[5:3000, 0, 1]
b150 = b150_nan[~np.isnan(b150_nan)]
b150_mean = np.mean(b150)
b150_std = np.std(b150)

c50_nan = c50pos[5:3000, 0, 1]
c50 = c50_nan[~np.isnan(c50_nan)]
c50_mean = np.mean(c50)
c50_std = np.std(c50)

c100_nan = c100pos[5:3000, 0, 1]
c100 = c100_nan[~np.isnan(c100_nan)]
c100_mean = np.mean(c100)
c100_std = np.std(c100)

c150_nan = c150pos[5:3000, 0, 1]
c150 = c150_nan[~np.isnan(c150_nan)]
c150_mean = np.mean(c150)
c150_std = np.std(c150)

d50_nan = d50pos[5:3000, 0, 1]
d50 = d50_nan[~np.isnan(d50_nan)]
d50_mean = np.mean(d50)
d50_std = np.std(d50)

d100_nan = d100pos[5:3000, 0, 1]
d100 = d100_nan[~np.isnan(d100_nan)]
d100_mean = np.mean(d100)
d100_std = np.std(d100)

d150_nan = d150pos[5:3000, 0, 1]
d150 = d150_nan[~np.isnan(d150_nan)]
d150_mean = np.mean(d150)
d150_std = np.std(d150)

#Chart values

Recordings = ['2,5cm','5cm', '10cm', '15cm']
count = np.arange(len(Recordings))

#sorting means

means = [a50_mean, a100_mean, a150_mean, b50_mean, b100_mean, b150_mean, c50_mean, c100_mean, c150_mean, d50_mean, d100_mean, d150_mean]
means50 = means[::3]
means100 = means[1::3]
means150 = means[2::3]

#sorting errors

error = [a50_std, a100_std, a150_std, b50_std, b100_std, b150_std, c50_std, c50_std, c50_std, d50_std, d100_std, d150_std]
error50 = error[::3]
error100 = error[1::3]
error150 = error[2::3]

width = 0.35

# names = ['Fish_a','Fish_b','Fish_d']
# values = [a,b,d]

fig, ax = plt.subplots()

rects1 = ax.bar(count - width/3, means50, width/3, yerr=error50, align='center', alpha=0.8, ecolor='blue', capsize=4, label='0,5x scaling')
rects2 = ax.bar(count, means100, width/3, yerr=error100, align='center', alpha=0.8, ecolor='red', capsize=4, label='1x scaling')
rects3 = ax.bar(count + width/3, means150, width/3, yerr=error150, align='center', alpha=0.8, ecolor='green', capsize=4, label='1,5x scaling')

#Plotting Axes

#ax.bar(count, means, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=5)
ax.set_xticks(count)
ax.set_xticklabels(Recordings)
ax.yaxis.grid(True)
ax.set_ylabel('Distance from Water surface')
ax.set_xlabel('Waterlevel')
ax.set_title('Swimmingheight in dependency of Waterlevel')
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 10),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.tight_layout()
plt.show()
