# import numpy as np
from matplotlib import pyplot as plt
import random
# import math

# Parameters to be used for the integrate and fire equation
deltaT = 1  # timestep [ms]
totalTime = 1000 # taking time in [ms]


synapses = []
rate = 10  # firing rate [Hz]
i = 0  # index denoting which element of V is being assigned

for synapse in range(40):
	spikeTrain = []
	spikeTimes = []
	for index in range(totalTime):
	    if (rate * deltaT) / 1000 >= random.uniform(0,1):
	        spikeTrain.append(-50)
	    else:
	        spikeTrain.append(-65)
	    spikeTimes.append(index)

	synapses.append(spikeTrain)


plt.plot(spikeTimes, synapses[20])
plt.xlabel("Spike time [ms]", fontsize=15)
plt.ylabel("Voltage [mV]", fontsize=15)
plt.title("Skipe Train", fontsize=20)
plt.show()
