# Importing modules of serial, numpy, matplotlib, math and csv

import serial
import numpy as np
import matplotlib.pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D
import math
import csv

# Dimensions of the data matrix
x_size = 40
y_size = 40
totalData_size = x_size * y_size

data = []
expectedDistance = []
servoAngles = []

x_scatter = []
y_scatter = []
z_scatter = []

x_final = []
y_final = []
z_final = []

# Connects Python to the serial port
ser = serial.Serial('/dev/ttyACM2',9600)

# Loops through all the data points - 1st and 2nd line = servo angles (degrees), 3rd line = voltage reading
for x in range(totalData_size):
	servoAngles.append(( float(ser.readline()), float(ser.readline()) ))
	data.append(float(ser.readline()))
	
	### print data[x], servoAngles[x]

# Converts the voltages to distances using the calibration function
a = 372.2
b = -3.962
c = 99.51
d = -0.6113

for i in data:
	expectedDistance.append(a * math.exp(b * i) + c * math.exp(d * i))

# Meshgrid of x and y array
x_scatter = range(totalData_size)
x_scatter = [n/x_size for n in x_scatter]
y_scatter = range(y_size) * x_size

# Saves the data to a csv file
csv_file = open("data.csv", "wb")
csv_writer = csv.writer(csv_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for i in range(totalData_size):
	csv_writer.writerow([x_scatter[i], y_scatter[i], expectedDistance[i]])

# Filters out data points that are more than 100 cm away
for i in range(totalData_size):
	if expectedDistance[i] < 100:
		x_final.append(x_scatter[i])
		y_final.append(y_scatter[i])
		z_final.append(expectedDistance[i])

# Scatter plot of the final data.
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_final, y_final, z_final)
plt.show()
