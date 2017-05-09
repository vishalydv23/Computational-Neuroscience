import numpy as np
from matplotlib import pyplot as plt
	
# Parameters for integrate and fire equation
deltaT = 1 #timestep [ms]
totalTime = 1000 #total time [ms]
E_L = -70 #resting voltage [mV]
V_Th = -40 #Threshold voltage [mV]
Rm = 10 #membrane resistance [Mohm]
tau = 10; # time constant [ms]

g_k = 0.005 # (MOhm)^-1
tau_k = 200
E_K = -80.0 # [mV]

n = int(totalTime / deltaT)

#initial vector to hold value
time = np.linspace(0,totalTime, n+1) #will hold vector of times
Voltage = np.zeros(len(time))  #initialize the voltage vector.

i = 0; #index denoting which element of V is being assigned
Voltage[i]=E_L; #value of V at t=0

I_e = 3.1; #injected current [nA]

for index in range(totalTime):
	dg_k = ((-1 * g_k) / tau_k) * deltaT
	g_k = g_k + dg_k 
	dv = ((-Voltage[index] + E_L + (I_e * Rm) - ((Rm * g_k) * (E_K - Voltage[index])))/tau) * deltaT
	Voltage[index + 1] = Voltage[index] + dv

	if(Voltage[index + 1] > V_Th):
		Voltage[index + 1] = E_L;

plt.plot(time,Voltage)
plt.xlabel("Time in ms")
plt.ylabel("Voltage in mV")
plt.title("Voltage vs. time (With slow potassium current)")
plt.show()

