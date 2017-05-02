import matplotlib.pyplot as plt
import numpy as np
import collections
import matplotlib.gridspec as gridspec

# loading neuron 1 - 4 
csvneuron4 = open("data/neuron4.csv")
neuron4 = list(map( lambda x: int(x.strip()), csvneuron4.readlines() ))

# loading the time data  from csv file
csv_time = open("data/time.csv")
time = list(map( lambda x: int(x.strip()), csv_time.readlines() ))

# loading x and y using the provided code snippets
csv_x = open("data/x.csv")
x = list(map( lambda x: float(x.strip()), csv_x.readlines() ))
csv_y = open("data/y.csv")
y = list(map( lambda x: float(x.strip()), csv_y.readlines() ))

index = 0;

neuron4_Right_Up = [];
neuron4_Left_Up = [];
neuron4_Right_Down = [];
neuron4_Left_Down = [];
neuron4_Center = [];

modifiedTime = []
countList1 = []
countList2 = []
countList3 = []
countList4 = []
countList5 = []

for spikeTime in neuron4:
	if(spikeTime in time):
		index = time.index(spikeTime)
	else:
		nearestValue = min(time, key=lambda x:abs(x-spikeTime))
		index = time.index(nearestValue)

	if(x[index] > 195 and y[index] > 140):
		neuron4_Right_Up.append(spikeTime)
	elif(x[index] < 145 and y[index] > 140):
		neuron4_Left_Up.append(spikeTime)
	elif(x[index] > 195 and y[index] < 80):
		neuron4_Right_Down.append(spikeTime)
	elif(x[index] < 145 and y[index] < 80):
		neuron4_Left_Down.append(spikeTime)
	else:
		neuron4_Center.append(spikeTime)


for i in range(0,len(time)):
	time[i] = int(round(time[i]/10000))

for i in range(0,len(neuron4_Right_Up)):
	neuron4_Right_Up[i] = int(round(neuron4_Right_Up[i]/10000))
for i in range(0,len(neuron4_Left_Up)):
	neuron4_Left_Up[i] = int(round(neuron4_Left_Up[i]/10000))
for i in range(0,len(neuron4_Right_Down)):
	neuron4_Right_Down[i] = int(round(neuron4_Right_Down[i]/10000))
for i in range(0,len(neuron4_Left_Down)):
	neuron4_Left_Down[i] = int(round(neuron4_Left_Down[i]/10000))
for i in range(0,len(neuron4_Center)):
	neuron4_Center[i] = int(round(neuron4_Center[i]/10000))


counter_RU=collections.Counter(neuron4_Right_Up)
counter_LU=collections.Counter(neuron4_Left_Up)
counter_RD=collections.Counter(neuron4_Right_Down)
counter_LD=collections.Counter(neuron4_Left_Down)
counter_C=collections.Counter(neuron4_Center)

for i in range(time[0],time[len(time)-1]):
	modifiedTime.append(i)
	if i in neuron4_Right_Up:
		countList1.append(counter_RU[i])
	else:
		countList1.append(0)
	if i in neuron4_Left_Up:
		countList2.append(counter_LU[i])
	else:
		countList2.append(0)
	if i in neuron4_Right_Down:
		countList3.append(counter_RD[i])
	else:
		countList3.append(0)
	if i in neuron4_Left_Down:
		countList4.append(counter_LD[i])
	else:
		countList4.append(0)
	if i in neuron4_Center:
		countList5.append(counter_C[i])
	else:
		countList5.append(0)


plt.figure(0)
ax2 = plt.subplot2grid((3,4), (0,0),colspan=2)
plt.plot(modifiedTime,countList2, label='Firing rate in F1 (Left Upper Region)')
plt.ylabel("Firing Rate in Hz")
ax2.legend(loc="upper right")

ax1 = plt.subplot2grid((3,4), (0,2), colspan=2)
plt.plot(modifiedTime,countList1, label='Firing rate in C1 (Right Upper Region)')
ax1.legend(loc="upper right")


ax5 = plt.subplot2grid((3,4), (1, 0), colspan=4)
plt.plot(modifiedTime,countList5, label='Firing rate in connection (Center Region)')
plt.ylabel("Firing Rate in Hz")
ax5.legend(loc="upper right")

ax4 = plt.subplot2grid((3,4), (2, 0), colspan=2)
plt.plot(modifiedTime,countList4, label='Firing rate in F2 (Left Down Region)')
plt.xlabel("Time in second ranging from 3198 sec to 4286 sec")
plt.ylabel("Firing Rate in Hz")
ax4.legend(loc="upper right")

ax3 = plt.subplot2grid((3,4), (2, 2), colspan=2)
plt.plot(modifiedTime,countList3, label='Firing rate in C2 (Right Down Region)')
plt.xlabel("Time in second ranging from 3198 sec to 4286 sec")
ax3.legend(loc="upper right")

plt.suptitle("Firing rates of neuron 4 in different part of the maze")
plt.show()

