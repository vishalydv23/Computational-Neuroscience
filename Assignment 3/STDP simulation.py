import numpy as np
from matplotlib import pyplot as plt
import random
import math

deltaT = 1  # time step [ms]
totalTime = 1000 * 20  # taking time in [ms]
i = 0  # index denoting which element of V is being assigned
# *************************************1st simulation variables*******************************************************

# Parameters to be used for the integrate and fire equation
E_L = -65.0  # resting voltage [mV]
V_reset = -65.0  # reset voltage [mV]
V_Th = -50.0  # Threshold voltage  [mV]
Rm = 100  # membrane resistance [Mohm]
tau_m = 10  # time constant [ms]
C = 0.1  # [nF]
g_syn = random.uniform(0, 2.0)  # initial peak conductance [nS]
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
rate = 10  # firing rate [Hz]

# *****************************************3rd simulation variables****************************************************

A_Plus = 0.1  # [nS]
A_minus = 0.12  # [nS]
Tau_plus = 20  # [ms]
Tau_minus = 20  # [ms]

# default state of the STDP
Flag = 1
# *****************************************setting up synapse**********************************************************
# storing spike train of 40 synapses
for synapse in range(40):
	spikeTrain = []
	spikeIndex = []
	spikeTimes = []
	for index in range(totalTime):
		if (rate * deltaT) / 1000 >= random.uniform(0,1):
			spikeTrain.append(-50)
			spikeIndex.append(index)
		else:
			spikeTrain.append(-65)
		spikeTimes.append(index)

	synapses.append(spikeTrain)

# *******************************************setting up the neuron*****************************************************
# setting up the neuron
voltage_indexlist = []
spike_flag = 0  # work as an indicator of spike. 0 as no and 1 means yes
spike_counter = 0
time_diff = 0
plasticityVariable = 0

for index in range(totalTime):
	if spike_flag == 1:
		spike_flag = 0
		if(time_diff > 0):
			plasticityVariable = A_Plus * math.exp(-1 * (abs(time_diff) / Tau_plus))
		else:
			plasticityVariable = A_minus * math.exp(-1 * (abs(time_diff) / Tau_minus))
		
	d_g_syn = g_syn * math.exp(-1 * (deltaT / tau_s)) * deltaT + plasticityVariable
	G_syn = G_syn + d_g_syn  # conductance
	# if(G_syn < 0):
	# 	G_syn = 0
	# elif(G_syn > 2):
	# 	G_syn = 2
	I_e = (40 * G_syn * ((E_s - Voltage[index]) * 0.000001)) #input current
	V_Themp = E_L + I_e * Rm
	Voltage[index + 1] = V_Themp + (Voltage[index] - V_Themp) * np.exp(- deltaT / tau_m)

	if(Voltage[index + 1] > V_Th):
		Voltage[index + 1] = V_reset
		G_syn = 0
		if(spike_counter < len(spikeIndex)):
			time_diff = index - spikeIndex[spike_counter]
			spike_counter += 1
			spike_flag = 1
			
		# voltage_indexlist.append(index)

# **********************************************STPD*******************************************************************
# min_length = (min(len(spikeIndex), len(voltage_indexlist)))
# time_diff = 0

# for index in range(min_length):
# 	time_diff = voltage_indexlist[index] - 

plt.plot(time, Voltage)
plt.xlabel("Time in ms")
plt.ylabel("Voltage in mV")
plt.title("Excitatory Synapse with Equilibrium Potential 0.0")
plt.show()