
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py

line = plt.figure()

np.random.seed(5)
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)
plt.plot(x, y, "o")


# draw vertical line from (70,100) to (70, 250)
plt.plot([70, 70], [100, 250], 'k-', lw=2)

# draw diagonal line from (70, 90) to (90, 200)
plt.plot([70, 90], [90, 200], 'k-')

# plot_url = py.plot_mpl(line, filename='mpl-docs/add-line')