import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pickle

filepath = 'E:/rec/swimheight_all/swimheight_light_5cm_Scale50pc.pickle'
with open(filepath, 'rb') as file:
    data = pickle.load(file)
    positions = data['positions']
    times = data['time']

pos = np.nan * np.ones((len(positions), 50, 2))
for i, c in enumerate(positions):
    for j, cc in enumerate(c):
        if cc[1] < 0 or cc[1] > 5:
            pos[i, j, :] = [np.nan, np.nan]
        else:
            pos[i, j, :] = cc

a = pos[5:3000,0,1]



        #if cc[1]

# pos ist die Variable wie aus dem Beispielcode den wir besprochen haben

fig = plt.figure()
for i in range(4):
    new_y = pos[:,i,1] # Waehle alle y-Positionen fuer diesen Partikel aus
    y_differences = np.diff(new_y) # Differenzen der y Positionen (dieses Array ist um 1 kuerzer als die Anzahl der Frames)
    y_differences[np.isnan(y_differences)] = np.inf
#    threshold = np.percentile(y_differences, 99) # Schwellenwert
    threshold = 1
    boolvec = y_differences > threshold # Bool'scher Vektor
    boolvec = np.append(False, boolvec) # Fuege einen False Wert zu Beginn des Vektors hinzu, weil er 1 kuerzer ist als die 1. Dimension von Variable pos

    new_y[boolvec] = np.nan # Ersetze alle y-Werte ueber der Schwelle durch NaNs

    plt.plot(times[5:3000], new_y[5:3000], '--', alpha=0.4)
plt.show()