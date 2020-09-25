import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pickle

#Chart values

Recordings = ['2,5cm','5cm', '10cm', '15cm']
#Recordings = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
count = np.arange(len(Recordings))

#sorting means

means = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
means50 = means[::3]
means100 = means[1::3]
means150 = means[2::3]

#sorting errors

error = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
error50 = error[::3]
error100 = error[1::3]
error150 = error[2::3]

width = 0.6

# names = ['Fish_a','Fish_b','Fish_d']
# values = [a,b,d]

fig, ax = plt.subplots()

rects1 = ax.bar(count - width/3, means50, width/3, yerr=error50, align='center', alpha=0.8, ecolor='blue', capsize=4, label='0,5x scaling')
rects2 = ax.bar(count, means100, width/3, yerr=error50, align='center', alpha=0.8, ecolor='red', capsize=4, label='1x scaling')
rects3 = ax.bar(count + width/3, means150, width/3, yerr=error50, align='center', alpha=0.8, ecolor='green', capsize=4, label='1,5x scaling')


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