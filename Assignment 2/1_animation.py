import numpy as np
import matplotlib.pyplot as plt

csv_time = open("data/time.csv")
time = list(map( lambda x: int(x.strip()), csv_time.readlines() ))

# loading x and y using the provided code snippets
csv_x = open("data/x.csv")
x = list(map( lambda x: float(x.strip()), csv_x.readlines() ))
csv_y = open("data/y.csv")
y = list(map( lambda x: float(x.strip()), csv_y.readlines() ))

index = 0;
x_coordinate = [];
y_coordinate = [];

fig, ax = plt.subplots()

for t in range(0, len(time)-1):
	x_coordinate.append(x[t])
	y_coordinate.append(y[t])
	if(t%50 == 0):
		points, = ax.plot(x_coordinate, y_coordinate, 'mo', markeredgecolor='black', alpha=0.2)
		plt.title("Animation of traveling of rat in maze", fontsize=25)
		plt.xlabel('X Coordinate of maze', fontsize=20)
		plt.ylabel('Y Coordinate of maze', fontsize=20)
		plt.pause(0.5)

