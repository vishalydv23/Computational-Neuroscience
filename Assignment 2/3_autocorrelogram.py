import matplotlib.pyplot as plt
import numpy as np

csvneuron1 = open("data/neuron1.csv")
neuron1 = list(map( lambda x: int(x.strip()), csvneuron1.readlines() ))

csvneuron2 = open("data/neuron2.csv")
neuron2 = list(map( lambda x: int(x.strip()), csvneuron2.readlines() ))

csvneuron3 = open("data/neuron3.csv")
neuron3 = list(map( lambda x: int(x.strip()), csvneuron3.readlines() ))

csvneuron4 = open("data/neuron4.csv")
neuron4 = list(map( lambda x: int(x.strip()), csvneuron4.readlines() ))

# neuron1Sec = []
# neuron2Sec = []
# neuron3Sec = []
# neuron4Sec = []

# for i in range(0,len(neuron1)):
# 	neuron1Sec.append(int(round(neuron1[i]/10000)))

# for i in range(0,len(neuron2)):
# 	neuron2Sec.append(int(round(neuron2[i]/10000)))

# for i in range(0,len(neuron3)):
# 	neuron3Sec.append(int(round(neuron3[i]/10000)))

# for i in range(0,len(neuron4)):
# 	neuron4Sec.append(int(round(neuron4[i]/10000)))

def acorr(n):
	n = n - np.mean(n)
	result = np.correlate(n , n, mode ='full')[len(n)-1:]

	result /= np.max(result)
	return result

neuron1Outcome = acorr(neuron1)
# neuron1SecOutcome = acorr(neuron1Sec)
neuron2Outcome = acorr(neuron2)
# neuron2SecOutcome = acorr(neuron2Sec)
neuron3Outcome = acorr(neuron3)
# neuron3SecOutcome = acorr(neuron3Sec)
neuron4Outcome = acorr(neuron4)
# neuron4SecOutcome = acorr(neuron4Sec)

# ax2 = plt.subplot2grid((2,1), (0,0))
plt.plot(neuron1Outcome)
plt.title("Auto Correlogram of neuron 1", fontsize=20)
plt.xlabel('Lags', fontsize=15)
plt.ylabel('Auto-Correlation', fontsize=15)

# ax1 = plt.subplot2grid((2,1), (1,0))
# plt.plot(neuron1SecOutcome)
# plt.xlabel('Lags', fontsize=15)
# plt.ylabel('Auto-Correlation', fontsize=15)
plt.show()

# plt.figure(0)
# ax2 = plt.subplot2grid((2,1), (0,0))
plt.plot(neuron2Outcome)
plt.title("Auto Correlogram of neuron 2", fontsize=20)
plt.xlabel('Lags', fontsize=15)
plt.ylabel('Auto-Correlation', fontsize=15)

# ax1 = plt.subplot2grid((2,1), (1,0))
# plt.plot(neuron2SecOutcome)
# plt.xlabel('Lags', fontsize=15)
# plt.ylabel('Auto-Correlation', fontsize=15)
plt.show()

# plt.figure(0)
# ax2 = plt.subplot2grid((2,1), (0,0))
plt.plot(neuron3Outcome)
plt.title("Auto Correlogram of neuron 3", fontsize=20)
plt.xlabel('Lags', fontsize=15)
plt.ylabel('Auto-Correlation', fontsize=15)

# ax1 = plt.subplot2grid((2,1), (1,0))
# plt.plot(neuron3SecOutcome)
# plt.xlabel('Lags', fontsize=15)
# plt.ylabel('Auto-Correlation', fontsize=15)
plt.show()

# plt.figure(0)
# ax2 = plt.subplot2grid((2,1), (0,0))
plt.plot(neuron4Outcome)
plt.title("Auto Correlogram of neuron 4", fontsize=20)
plt.xlabel('Lags', fontsize=15)
plt.ylabel('Auto-Correlation', fontsize=15)

# ax1 = plt.subplot2grid((2,1), (1,0))
# plt.plot(neuron4SecOutcome)
# plt.xlabel('Lags', fontsize=15)
# plt.ylabel('Auto-Correlation', fontsize=15)
plt.show()
