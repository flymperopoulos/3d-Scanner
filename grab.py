import serial
import numpy as np
import matplotlib.pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D

# time.sleep(1.5)

ser = serial.Serial('/dev/tty.usbmodemfd121',9600)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

data = [0] * 900
max_data = 0

for x in range(900):
	data[x] = float(ser.readline())
	if data[x] > max_data:
		max_data = data[x]
	print data[x]

for i in range(900):
	data[i] = data[i] / max_data


y_scatter = range(30) * 30
x_scatter = range(900)
x_scatter = [n/30 for n in x_scatter]

ax.scatter(x_scatter, y_scatter, data)
plt.show()