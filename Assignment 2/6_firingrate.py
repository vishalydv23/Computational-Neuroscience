import numpy as np
from matplotlib import pyplot as plt
import collections

csvneuron1 = open("data/neuron1.csv")
neuron1 = list(map( lambda x: int(x.strip()), csvneuron1.readlines() ))

# loading the time data  from csv file
csv_time = open("data/time.csv")
time = list(map( lambda x: int(x.strip()), csv_time.readlines() ))

modifiedTime = []
countList = []

for i in range(0,len(time)):
	time[i] = int(round(time[i]/10000))

for i in range(0,len(neuron1)):
	neuron1[i] = int(round(neuron1[i]/10000))

counter=collections.Counter(neuron1)

# print(counter[3516])
for i in range(time[0],time[len(time)-1]):
	modifiedTime.append(i)
	if i in neuron1:
		countList.append(counter[i])
	else:
		countList.append(0)

plt.plot(modifiedTime,countList)
plt.xlabel("Time in second (3198 sec - 4286 sec)", fontsize=15)
plt.xticks(np.arange(np.min(modifiedTime), np.max(modifiedTime)+1, 100.0))
plt.ylabel("Firing Rate in Hz", fontsize=15)
plt.yticks(np.arange(np.min(countList), np.max(countList)+1, 2.0))
plt.title("Firing rate of neuron 1 per second", fontsize=20)
plt.show()

csvneuron2 = open("data/neuron2.csv")
neuron2 = list(map( lambda x: int(x.strip()), csvneuron2.readlines() ))


modifiedTime = []
countList = []

for i in range(0,len(neuron2)):
	neuron2[i] = int(round(neuron2[i]/10000))

counter=collections.Counter(neuron2)

# print(counter[3516])
for i in range(time[0],time[len(time)-1]):
	modifiedTime.append(i)
	if i in neuron1:
		countList.append(counter[i])
	else:
		countList.append(0)

plt.plot(modifiedTime,countList)
plt.xlabel("Time in second (3198 sec - 4286 sec)", fontsize=15)
plt.xticks(np.arange(np.min(modifiedTime), np.max(modifiedTime)+1, 100.0))
plt.ylabel("Firing Rate in Hz", fontsize=15)
plt.yticks(np.arange(np.min(countList), np.max(countList)+1, 1.0))
plt.title("Firing rate of neuron 2 per second", fontsize=20)
plt.show()

csvneuron3 = open("data/neuron3.csv")
neuron3 = list(map( lambda x: int(x.strip()), csvneuron3.readlines() ))

modifiedTime = []
countList = []

for i in range(0,len(neuron3)):
	neuron3[i] = int(round(neuron3[i]/10000))

counter=collections.Counter(neuron3)

# print(counter[3516])
for i in range(time[0],time[len(time)-1]):
	modifiedTime.append(i)
	if i in neuron1:
		countList.append(counter[i])
	else:
		countList.append(0)

plt.plot(modifiedTime,countList)
plt.xlabel("Time in second (3198 sec - 4286 sec)", fontsize=15)
plt.xticks(np.arange(np.min(modifiedTime), np.max(modifiedTime)+1, 100.0))
plt.ylabel("Firing Rate in Hz", fontsize=15)
plt.yticks(np.arange(np.min(countList), np.max(countList)+1, 1.0))
plt.title("Firing rate of neuron 3 per second", fontsize=20)
plt.show()

csvneuron4 = open("data/neuron4.csv")
neuron4 = list(map( lambda x: int(x.strip()), csvneuron4.readlines() ))

modifiedTime = []
countList = []

for i in range(0,len(neuron4)):
	neuron4[i] = int(round(neuron4[i]/10000))

counter=collections.Counter(neuron4)

# print(counter[3516])
for i in range(time[0],time[len(time)-1]):
	modifiedTime.append(i)
	if i in neuron4:
		countList.append(counter[i])
	else:
		countList.append(0)

plt.plot(modifiedTime,countList)
plt.xlabel("Time in second (3198 sec - 4286 sec)", fontsize=15)
plt.xticks(np.arange(np.min(modifiedTime), np.max(modifiedTime)+1, 100.0))
plt.ylabel("Firing Rate in Hz", fontsize=15)
plt.yticks(np.arange(np.min(countList), np.max(countList)+1, 2.0))
plt.title("Firing rate of neuron 4 per second", fontsize=20)
plt.show()