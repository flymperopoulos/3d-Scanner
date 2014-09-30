import serial
import numpy as np
import matplotlib.pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D
import math
import csv

x_size = 40
y_size = 40
totalData_size = x_size * y_size
data = [0] * totalData_size
max_data = 0
expectedDistance = []
servoAngles = []

x_scatter = []
y_scatter = []
z_scatter = []

x_final = []
y_final = []
z_final = []

ser = serial.Serial('/dev/ttyACM2',9600)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


for x in range(totalData_size):
	servoAngles.append(( float(ser.readline())*math.pi/180.0, float(ser.readline())*math.pi/180.0 ))
	data[x] = float(ser.readline())
	if data[x] > max_data:
		max_data = data[x]
	print data[x], servoAngles[x]

for i in range(totalData_size):
	data[i] = data[i] / max_data

a = 372.2
b = -3.962
c = 99.51
d = -0.6113

for i in data:
	expectedDistance.append(a * math.exp(b * i) + c * math.exp(d * i))

x_scatter = range(totalData_size)
x_scatter = [n/x_size for n in x_scatter]
y_scatter = range(y_size) * x_size

csv_file = open("data.csv", "wb")
csv_writer = csv.writer(csv_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for i in range(totalData_size):
	csv_writer.writerow([x_scatter[i], y_scatter[i], expectedDistance[i]])

print expectedDistance

for i in range(totalData_size):
	if expectedDistance[i] < 100:
		x_final.append(x_scatter[i])
		y_final.append(y_scatter[i])
		z_final.append(expectedDistance[i])

# for i in range(totalData_size):
# 	x_scatter.append(expectedDistance[i] * np.cos(servoAngles[i][0]) * np.sin(servoAngles[i][1]))
# 	y_scatter.append(expectedDistance[i] * np.sin(servoAngles[i][0]) * np.sin(servoAngles[i][1]))
# 	z_scatter.append(expectedDistance[i] * np.cos(servoAngles[i][1]))

ax.scatter(x_final, y_final, z_final)
plt.show()
