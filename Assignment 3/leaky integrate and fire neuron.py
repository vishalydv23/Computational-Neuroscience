import numpy as np
from matplotlib import pyplot as plt
import random
import math

# Parameters to be used for the integrate and fire equation
deltaT = 1 #timestep [ms]
totalTime = 1000 * 200#taking time in [ms]
E_L = -65.0 #resting voltage [mV]
V_reset = -65.0 #reset voltage [mV]
V_Th = -50.0 # Threshold voltage  [mV]
Rm = 100 #membrane resistance [Mohm]
tau_m = 10 # time constant [ms]


C = 0.1  # [nF]
g_syn = random.uniform(0, 2.0)  # initial peak conductance [nS]
G_syn = 0
tau_s = 2.0  # time constant of synapse[ms]
T_f = 0  #when did the presynaptic neuron last fire?


# Asuming synapses are Inhibitory
E_s = 0.0  # [mV]


n = int(totalTime / deltaT)

# initial vector to hold value
time = np.linspace(0,totalTime, n+1)  # will hold vector of times
Voltage = np.zeros(len(time))  # vector of voltage

i = 0  # index denoting which element of V is being assigned
Voltage[i] = E_L  # value of V at t=0

for index in range(totalTime):

  d_g_syn = g_syn * math.exp(-1 * (deltaT / tau_s)) * deltaT
  G_syn = G_syn + d_g_syn  # conductance
  I_e = (40 * G_syn * ((E_s - Voltage[index]) * 0.000001)) #input current

  V_Themp = E_L + I_e * Rm

  Voltage[index + 1] = V_Themp + (Voltage[index] - V_Themp) * np.exp(- deltaT / tau_m)

  if(Voltage[index + 1] > V_Th):
    Voltage[index + 1] = V_reset
    G_syn = 0
    # T_f = index

plt.plot(time, Voltage)
plt.xlabel("Time in ms")
plt.ylabel("Voltage in mV")
plt.title("Excitatory Synapse with Equilibrium Potential 0.0")
plt.show()

