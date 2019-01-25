import numpy as np
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
from random import randint
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

#cekjarak

def cekjarak(X1,Y1, X2, Y2):
    dest = ((X1 - X2)**2 + (Y1 - Y2)**2)**0.5
    return dest

#gula
paramsgula = 2
gula = 5
position = np.zeros([gula, paramsgula])
for i in range(gula):
    position[i][0] = randint(-2, 2)
    position[i][1] = randint(-2, 2)
    for j in range(i):
        if position[i][0] == position[j][0] and position[i][1] == position[j][1]:
            position[i][0] = randint(-2, 2)
            position[i][1] = randint(-2, 2)

tmax = 200
c1 = 0.001
c2 = 0.002
levels = np.linspace(-1, 35, 100)

#semut
paramsemut = 2
semut = 10
position1 = np.zeros([semut, paramsemut])
for i in range(semut):
    position1[i][0] = random.uniform(3, 3.5)
    position1[i][1] = random.uniform(3, 3.5)
#position1[0][0] = 3
#position1[0][1] = 3
#position1[1][0] = -2.92
#position1[1][1] = -2.88
#position1[2][0] = 2.84
#position1[2][1] = 2.84
#position1[3][0] = -2.96
#position1[3][1] = -2.25
velocity = np.zeros([semut, paramsemut])

jarak = []
prev = []
index = []
for i in range(semut):
    jarak.append(0)
    prev.append(0)
    index.append(0)
sekon = 10
cek = False
jumlah = 0

for i in range(semut):
    jarak[i] = 100
    prev[i] = 0
    index[i] = 0
    for j in range(gula):
        temp = cekjarak(position1[i][0], position1[i][1], position[j][0], position[j][1])
        if jarak[i] > temp:
            prev[i] = jarak[i]
            jarak[i] = temp
            index[i] = j

count = []
nosemut1 = []
nosemut2 = []
for i in range(gula):
    count.append(0)
    nosemut1.append(-1)
    nosemut2.append(-1)

for t in range(tmax):
    for j in range(gula):
        if count[j] >= 2:
            cek = True
        elif count[j] < 2:
            cek = False
            break

    if cek == True:
        jumlah += 1

    for i in range(semut):
        #print(index[i])
        if jumlah <= 20:
            if count[index[i]] >= 2 and nosemut1[index[i]] != i and nosemut2[index[i]] != i:
                for j in range(gula):
                    if j != index[i] and count[j] < 2:
                        temp = cekjarak(position1[i][0], position1[i][1], position[j][0], position[j][1])
                        #print(j)
                        if jarak[i] > temp:
                            prev[i] = jarak[i]
                            jarak[i] = temp
                            index[i] = j

            if (position1[i][0] >= position[index[i]][0] - 0.3 and position1[i][0] <= position[index[i]][0] + 0.3) and (position1[i][1] >= position[index[i]][1] - 0.3 and position1[i][1] <= position[index[i]][1] + 0.3):
                count[index[i]] += 1
                if nosemut1[index[i]] == -1:
                    nosemut1[index[i]] = i
                elif nosemut2[index[i]] == -1:
                    nosemut2[index[i]] = i
                for j in range(semut):
                    if i != j:
                        jarak[j] = 100
                print(count[index[i]])
                print(nosemut1[index[i]])
                print(nosemut2[index[i]])
                print(" ")

            perpindahanx = position[index[i]][0] - position1[i][0]
            perpindahany = position[index[i]][1] - position1[i][1]
            magnitude = (perpindahanx**2 + perpindahany**2)**0.5
            normalx = perpindahanx / magnitude
            normaly = perpindahany / magnitude
            tempx = normalx / sekon
            tempy = normaly / sekon
            velocity[i][0] = tempx
            velocity[i][1] = tempy
            #print(velocity[i][0])
            #print(velocity[i][1])

            if position1[i][0] != position[index[i]][0] and position1[i][1] != position[index[i]][1]:
                position1[i] += velocity[i]

        elif jumlah > 20:
            perpindahanx = 3.5 - position1[i][0]
            perpindahany = 3.5 - position1[i][1]
            magnitude = (perpindahanx**2 + perpindahany**2)**0.5
            normalx = perpindahanx / magnitude
            normaly = perpindahany / magnitude
            tempx = normalx / sekon
            tempy = normaly / sekon
            velocity[i][0] = tempx
            velocity[i][1] = tempy
            position1[i] += velocity[i]

        fig = plt.figure()
        plt.gca().set_xlim([-3,3])
        plt.gca().set_ylim([-3,3])

        if jumlah <= 20:
            for i in range(gula):
                plt.plot(position[i][0], position[i][1], 'ro')
            
        for i in range(semut):
            plt.plot(position1[i][0], position1[i][1], 'go')
        #plt.plot(global_best_position[0], global_best_position[1], 'ro')
        
        plt.title('{0:03d}'.format(t))
        filename = 'img{0:03d}.png'.format(t)
        plt.savefig(filename, bbox_inches='tight')
        plt.close(fig)
