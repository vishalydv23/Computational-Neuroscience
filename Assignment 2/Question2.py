import matplotlib.pyplot as plt
import numpy as np
from _future_ import division

csvneuron1 = open("data/neuron1.csv")
neuron1 = list(map( lambda x: int(x.strip()), csvneuron1.readlines() ))

# def acorr(x, ax=None):
# 	if ax is None:
# 		ax = plt.gca()
# 	autocorr = np.correlate(x,x,mode='full')
# 	autocorr /= autocorr.max()

# 	return autocorr

# # fig, ax = plt.subplot()
# plt.plot(acorr(neuron1))
# np.out(a)
# np.casting('unsafe')

plt.acorr(neuron1, maxlags=len(neuron1)-1)
plt.show()