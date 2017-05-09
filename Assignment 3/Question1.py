import numpy as np
from matplotlib import pyplot as plt
import random
import math

deltaT = 1  # time step [ms]
totalTime = 1000  * 200 # taking time in [ms]
i = 0  # index denoting which element of V is being assigned
# *************************************1st simulation variables*******************************************************

# Parameters to be used for the integrate and fire equation
E_L = -65.0  # resting voltage [mV]
V_reset = -65.0  # reset voltage [mV]
V_Th = -50.0  # Threshold voltage  [mV]
Rm = 100  # membrane resistance [Mohm]
tau_m = 10  # time constant [ms]
C = 0.1  # [nF]
# g_syn = random.uniform(0, 2.0)  # initial peak conductance [nS]
g_syn = 2.0
G_syn = 0
tau_s = 2.0  # time constant of synapse[ms]
T_f = 0  # when did the presynaptic neuron last fire?
# Asuming synapses are Inhibitory
E_s = 0.0  # [mV]
n = int(totalTime / deltaT)
# initial vector to hold value
time = np.linspace(0, totalTime, n+1)  # will hold vector of times
Voltage = np.zeros(len(time))  # vector of voltage
Voltage[i] = E_L  # value of V at t=0
# ****************************************2nd simulation variables*****************************************************
synapses = []
rate = 15  # firing rate [Hz]

# *****************************************3rd simulation variables****************************************************

A_Plus = 0.1  # [nS]
A_minus = 0.12  # [nS]
Tau_plus = 20  # [ms]
Tau_minus = 20  # [ms]

# *****************************************setting up synapse**********************************************************
spikeIndex = []

for synapse in range(40):
	for index in range(totalTime):
		if (rate * deltaT) / 1000 >= random.uniform(0,1):
			spikeIndex.append(index)

sortedlist = sorted(spikeIndex)
print(list(set(sortedlist)))
# *******************************************setting up the neuron*****************************************************
# setting up the neuron
voltage_indexlist = []
spike_flag = 0  # work as an indicator of spike. 0 as no and 1 means yes
spike_counter = 0
time_diff = 0
plasticityVariable = 0

neuron_spike_counter = 0 # count the spikes of post synaptic neuron
firingRate = 0
firingRateVector = []

# default state of the STDP
STDP_Flag = 0
synaptic_amplitude = 0 # synaptic applitude , 1 id added once spike is observed
T_f = 0 # last time when neuron observed spike

synapse = 0 # synaptic strength value
synapticstrength = []


for index in range(totalTime):
	if(index in spikeIndex):
		time_diff = T_f - index
		spike_flag = 1
	synaptic_amplitude = 0

	# if(index > totalTime/2):
	# 	STDP_Flag = 0 #STDP is switched on

	if spike_flag == 1: # if spike observed in neuron
		synaptic_amplitude = 1
		spike_flag = 0
		if(time_diff > 0):
			plasticityVariable = A_Plus * math.exp(-1 * (abs(time_diff) / Tau_plus))
		else:
			plasticityVariable = -1 * A_minus * math.exp(-1 * (abs(time_diff) / Tau_minus))
		synapse = synapse + synaptic_amplitude
	else:
		synapse = math.exp(-1 * (deltaT / tau_s)) * deltaT

	if(synapse < 0):
		synapse = 0
	elif(synapse > 2):
		synapse = 2

	synapse = 1.131388
	if(STDP_Flag == 0):
		plasticityVariable = 0

	synapticstrength.append(synapse)
	# synapse = math.exp(-1 * (deltaT / tau_s)) * deltaT 
	d_g_syn = g_syn * synapse + plasticityVariable
	G_syn = G_syn + d_g_syn  # conductance
	I_e = (40 * G_syn * ((E_s - Voltage[index]) * 0.000001)) #input current
	V_Themp = E_L + I_e * Rm
	Voltage[index + 1] = V_Themp + (Voltage[index] - V_Themp) * np.exp(- deltaT / tau_m)

	if(Voltage[index + 1] > V_Th):
		Voltage[index + 1] = V_reset
		G_syn = 0
		neuron_spike_counter += 1 
		if(spike_counter < len(spikeIndex)):
			time_diff = index - spikeIndex[spike_counter]
			spike_counter += 1
			synaptic_amplitude = spike_flag = 1
			T_f = index

	firingRate = (neuron_spike_counter / totalTime) * 1000 # firing rate in seconds
	firingRateVector.append(firingRate)

synapticstrength.append(synapticstrength[len(synapticstrength)-1]) # treating last value of synaptic strength , same as second last.
firingRateVector.append(firingRateVector[len(firingRateVector)-1])

print(np.mean(synapticstrength))
# plt.hist(synapticstrength)
# plt.plot(time, synapticstrength) # synaptic strength distribution
plt.plot(time, firingRateVector) # firing rate with stpd on
plt.grid()
plt.xlabel("time [ms]", fontsize = 15)
plt.ylabel("Firing rate", fontsize = 15)
plt.title("Firing rate of postsynaptic neuron (STDP on)", fontsize = 20)
plt.show()