import matplotlib.pyplot as plt
import numpy as np

# loading neuron 1 - 4 
csvneuron1 = open("data/neuron1.csv")
neuron1 = list(map( lambda x: int(x.strip()), csvneuron1.readlines() ))
csvneuron2 = open("data/neuron2.csv")
neuron2 = list(map( lambda x: int(x.strip()), csvneuron2.readlines() ))
csvneuron3 = open("data/neuron3.csv")
neuron3 = list(map( lambda x: int(x.strip()), csvneuron3.readlines() ))
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
x_neuron1 = [];
y_neuron1 = [];
x_neuron2 = [];
y_neuron2 = [];
x_neuron3 = [];
y_neuron3 = [];
x_neuron4 = [];
y_neuron4 = [];

for spikeTime in neuron1:
	if(spikeTime in time):
		index = time.index(spikeTime)
	else:
		nearestValue = min(time, key=lambda x:abs(x-spikeTime))
		index = time.index(nearestValue)
	x_neuron1.append(x[index])
	y_neuron1.append(y[index])

for spikeTime in neuron2:
	if(spikeTime in time):
		index = time.index(spikeTime)
	else:
		nearestValue = min(time, key=lambda x:abs(x-spikeTime))
		index = time.index(nearestValue)
	x_neuron2.append(x[index])
	y_neuron2.append(y[index])

for spikeTime in neuron3:
	if(spikeTime in time):
		index = time.index(spikeTime)
	else:
		nearestValue = min(time, key=lambda x:abs(x-spikeTime))
		index = time.index(nearestValue)
	x_neuron3.append(x[index])
	y_neuron3.append(y[index])

for spikeTime in neuron4:
	if(spikeTime in time):
		index = time.index(spikeTime)
	else:
		nearestValue = min(time, key=lambda x:abs(x-spikeTime))
		index = time.index(nearestValue)
	x_neuron4.append(x[index])
	y_neuron4.append(y[index])

p4, = plt.plot(x_neuron4, y_neuron4, 'mo', markeredgecolor='black', alpha=0.6)
p2, = plt.plot(x_neuron2, y_neuron2, 'go', markeredgecolor='black', alpha=0.6)
p1, = plt.plot(x_neuron1, y_neuron1, 'ro', markeredgecolor='black', alpha=0.6)
p3, = plt.plot(x_neuron3, y_neuron3, 'co', markeredgecolor='black', alpha=0.6)
plt.title("Position within map, where which each neuron was fired.", fontsize=20)
plt.xlabel('X Coordinate', fontsize=15)
plt.xticks(np.arange(np.min(x), np.max(x)+1, 20.0))
plt.ylabel('Y Coordinate', fontsize=15)
plt.yticks(np.arange(np.min(y), np.max(y)+1, 20.0))
plt.legend([p1, p2, p3, p4], ["Neuron 1", "Neuron 2", "Neuron 3", "Neuron 4"])
plt.show()