import numpy as np
from matplotlib import pyplot as plt
	
# Parameters for integrate and fire equation
deltaT = 1 #timestep [ms]
totalTime = 1000 #total time [ms]
E_L = -70 #resting voltage [mV]
V_Th = -40 #Threshold voltage [mV]
Rm = 10 #membrane resistance [Mohm]
tau = 10; # time constant [ms]

n = int(totalTime / deltaT)

#initial vector to hold value
time = np.linspace(0,totalTime, n+1) #will hold vector of times
Voltage = np.zeros(len(time))  #initialize the voltage vector.

i = 0; #index denoting which element of V is being assigned
Voltage[i]=E_L; #value of V at t=0

# tau*dV/dt = -V + E_L + I_e*R_m
# V(t) = E_L + R_m*I_e + [V(0) - E_l - R_m*I_e] * e(-t/tau)
I_e = 3.1; #injected current [nA]

for index in range(totalTime):
	V_Themp = E_L + I_e * Rm
	Voltage[index + 1] = V_Themp + (Voltage[index] - V_Themp) * np.exp(- deltaT / tau)

	if(Voltage[index + 1] > V_Th):
		Voltage[index + 1] = E_L;

plt.plot(time,Voltage)
plt.xlabel("Time in ms")
plt.ylabel("Voltage in mV")
plt.title("Voltage vs. time (Integrate and Fire Model)")
plt.show()

