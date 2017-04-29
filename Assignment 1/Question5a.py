# Simmulating 2 neurons connected by synapse

import numpy as np
from matplotlib import pyplot as plt
import random
import math

# Parameters to be used for the integrate and fire equation
deltaT = 1 #timestep [ms]
totalTime = 1000 #taking time in [ms]
E_L = -70 #resting voltage [mV]
V_reset = -80.0 #reset voltage [mV]
V_Th = -54.0 # Threshold voltage  [mV]
Rm = 10 #membrane resistance [Mohm]
tau = 20; # time constant [ms]

R_mG_s = 0.15 #[mV]
R_mI_e = 18.0 #[mV]
P_max = 0.5 
t_s = 10.0 # [ms]
T_f = 0; # when did the presynaptic neuron last fire?


# Asumming synapses are excitatory
E_s = 0.0 #[mV]


n = int(totalTime / deltaT)

#initial vector to hold value
time = np.linspace(0,totalTime, n+1) #will hold vector of times
VoltagePreSynaptic = np.zeros(len(time))  #initialize the VoltagePreSynaptic vector.
VoltagePostSynaptic = np.zeros(len(time))  #initialize the VoltagePreSynaptic vector.

i = 0; #index denoting which element of V is being assigned
VoltagePreSynaptic[i]= random.uniform(V_reset, V_Th) #value of V at t=0
VoltagePostSynaptic[i]= random.uniform(V_reset, V_Th)

# P_s = P_max * e(-1 * ((V - T_f)/ t_s)
# V(t) = ((- V + E_L + (Rm*I_e) - ((P_s * Rm * Gs) * (V - E_s)) ) / tau) * deltaT
for index in range(totalTime):

  P_sa = P_max * math.exp(-1 * ((index - T_f) / t_s))
  dV_a = ((E_L - VoltagePreSynaptic[index] - ((P_sa * R_mG_s) * (VoltagePreSynaptic[index] - E_s)) + (R_mI_e)) / tau) * deltaT
  VoltagePreSynaptic[index + 1] = VoltagePreSynaptic[index] + dV_a

  if(VoltagePreSynaptic[index + 1] > V_Th):
    VoltagePreSynaptic[index + 1] = V_reset
    T_f = index

  P_sb = P_max * math.exp(-1 * ((index - T_f) / t_s))
  dV_b = ((E_L - VoltagePostSynaptic[index] - ((P_sb * R_mG_s) * (VoltagePostSynaptic[index] - E_s)) + (R_mI_e)) / tau) * deltaT
  VoltagePostSynaptic[index + 1] = VoltagePostSynaptic[index] + dV_b

  if(VoltagePostSynaptic[index + 1] > V_Th):
    VoltagePostSynaptic[index + 1] = V_reset
    T_f = index

p1, = plt.plot(time,VoltagePreSynaptic, 'b')
p2, = plt.plot(time,VoltagePostSynaptic, 'r')
plt.xlabel("Time in ms")
plt.ylabel("Voltage in mV")
plt.title("Excitatory Synapse with Equilibrium Potential 0.0")
plt.legend([p2, p1], ["Neuron A", "Neuron B"])
plt.show()

