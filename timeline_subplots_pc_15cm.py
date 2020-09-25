import numpy as np
import matplotlib.pyplot as plt
import pickle
import matplotlib.gridspec as gridspec

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
prepend = 'E:/rec/pressurechange_all_1x/'
lowerbound, upperbound = 0, 11.6
atimes, apos = loadData('{}1_before_pressure_increase_15cm_1x_light.pickle'.format(prepend), lowerbound, upperbound)
btimes, bpos = loadData('{}2_pressure_increase_15cm_1x_light.pickle'.format(prepend), lowerbound, upperbound)
ctimes, cpos = loadData('{}3_after_pressure_increase_15cm_1x_light.pickle'.format(prepend), lowerbound, upperbound)
dtimes, dpos = loadData('{}4_pressure_decrease_15cm_1x_light.pickle'.format(prepend), lowerbound, upperbound)
etimes, epos = loadData('{}5_after_pressure_decrease_15cm_1x_light.pickle'.format(prepend), lowerbound, upperbound)

bstartindex = 90

a = apos[5:3000, 0, 1]
b = bpos[5:3000, 0, 1]
bt = btimes[5:3000]
c = cpos[5:3000, 0, 1]
d = dpos[5:3000, 0, 1]
e = epos[5:3000, 0, 1]

#f, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(4, 1, sharey=True, sharex=True, figsize=(12, 8))
fig1 = plt.figure(constrained_layout=True, figsize=(10,6))
gs = fig1.add_gridspec(3,4)
ax1 = fig1.add_subplot(gs[0, 1])
ax1.plot(a)
ax1.set_title('before PI')
ax2 = fig1.add_subplot(gs[0,2:4])
ax2.plot(bt-bt[bstartindex-5],b)
ax2.set_title('during PI')
ax3 = fig1.add_subplot(gs[1, 1])
ax3.plot(c)
ax3.set_title('after PI')
ax4 = fig1.add_subplot(gs[1, 2:4])
ax4.plot(d)
ax4.set_title('during PD')
ax5 = fig1.add_subplot(gs[2, 1:])
ax5.plot(e)
ax5.set_title('after PD')
ax5.set_xlabel('Time in Frames (5 Frames equals 1 Second)', fontsize='large')
fig1.suptitle('Example Fish of different Waterlevels')
fig1.text(0.08,0.28,'Distance from Watersurface (cm)', rotation='vertical', fontsize='large')

plt.show()
