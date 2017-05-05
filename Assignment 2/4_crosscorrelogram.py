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

# for i in range(0,len(neuron1)):
# 	neuron1[i] = int(round(neuron1[i]/10000))

# for i in range(0,len(neuron2)):
# 	neuron2[i] = int(round(neuron2[i]/10000))

# for i in range(0,len(neuron3)):
# 	neuron3[i] = int(round(neuron3[i]/10000))

# for i in range(0,len(neuron4)):
# 	neuron4[i] = int(round(neuron4[i]/10000))

def xcorr(n1, n2):
	n1 = n1 - np.mean(n1)
	n2 = n2 - np.mean(n2)
	result = np.correlate(n1 , n2, mode ='full')[len(n1)-1:]
	
	result /= np.max(result)
	return result

neuron12Outcome = xcorr(neuron1, neuron2)
neuron13Outcome = xcorr(neuron1, neuron3)
neuron14Outcome = xcorr(neuron1, neuron4)
neuron23Outcome = xcorr(neuron2, neuron3)
neuron24Outcome = xcorr(neuron2, neuron4)
neuron34Outcome = xcorr(neuron3, neuron4)


plt.plot(neuron12Outcome)
plt.title("Cross Correlogram of neuron 1 and neuron 2", fontsize=20)
plt.xlabel('Lags', fontsize=15)
plt.ylabel('Cross-Correlation', fontsize=15)
plt.show()

plt.plot(neuron13Outcome)
plt.title("Cross Correlogram of neuron 1 and neuron 3", fontsize=20)
plt.xlabel('Lags', fontsize=15)
plt.ylabel('Cross-Correlation', fontsize=15)
plt.show()

plt.plot(neuron14Outcome)
plt.title("Cross Correlogram of neuron 1 and neuron 4", fontsize=20)
plt.xlabel('Lags', fontsize=15)
plt.ylabel('Cross-Correlation', fontsize=15)
plt.show()

plt.plot(neuron23Outcome)
plt.title("Cross Correlogram of neuron 2 and neuron 3", fontsize=20)
plt.xlabel('Lags', fontsize=15)
plt.ylabel('Cross-Correlation', fontsize=15)
plt.show()

plt.plot(neuron24Outcome)
plt.title("Cross Correlogram of neuron 2 and neuron 4", fontsize=20)
plt.xlabel('Lags', fontsize=15)
plt.ylabel('Cross-Correlation', fontsize=15)
plt.show()

plt.plot(neuron34Outcome)
plt.title("Cross Correlogram of neuron 3 and neuron 4", fontsize=20)
plt.xlabel('Lags', fontsize=15)
plt.ylabel('Cross-Correlation', fontsize=15)
plt.show()