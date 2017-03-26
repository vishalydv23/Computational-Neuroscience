import numpy as np
from matplotlib import pyplot as plt
import math

# Parameters to be used for the integrate and fire equation
deltaT = 1 #timestep [ms]
totalTime = 1000 #taking time in [ms]
E_L = -70 #resting voltage [mV]
V_T = -40 # Threshold voltage  [mV]
Rm = 10 #membrane resistance [Mohm]
tau = 10; # time constant [ms]

n = int(totalTime / deltaT)

#initial vector to hold value
time = np.linspace(0,totalTime, n+1) #will hold vector of times
Voltage = np.zeros(len(time))  #initialize the voltage vector.

i = 0; #index denoting which element of V is being assigned
Voltage[i]=E_L; #first element of V, i.e. value of V at t=0

# tau*dV/dt = -V + E_L + I_e*R_m
# V(t) = E_L + R_m*I_e + [V(0) - E_l - R_m*I_e] * e(-t/tau)
I_e_Start = 2 # Current range start point [nA]
I_e_End = 5 # Current range end point [nA]
I_e_Steps = 0.1 # steps for current [nA]

I_e_Vector = np.linspace(I_e_Start, I_e_End, (I_e_End - I_e_Start) / I_e_Steps) # vector to store the different current value
i = 0 # counter

firingRateVector = np.zeros(len(I_e_Vector))  #firing rate vector

for I_e_value in I_e_Vector:

	SpikeCounter = 0 # This counts the number of spikes in model
	
	for index in range(totalTime):
		V_Temp = E_L + round(I_e_value,1) * Rm
		Voltage[index + 1] = V_Temp + (Voltage[index] - V_Temp) * np.exp(- deltaT / tau)

		if(Voltage[index + 1] > V_T): # if threshold is reached
			Voltage[index + 1] = E_L;
			SpikeCounter = SpikeCounter + 1

	firingRate = (SpikeCounter / totalTime) * 1000 # firing rate in seconds
	print("The firing rate for current = ", round(I_e_value,1) ," is:" , firingRate)

	firingRateVector[i] = firingRate
	i = i + 1

plt.plot(I_e_Vector,firingRateVector)
plt.xlabel("Current in nA")
plt.ylabel("Firing Rate in Hz")
plt.title("Firing Rate vs. Input Current")
plt.show()

