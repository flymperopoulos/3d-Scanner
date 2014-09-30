# Importing modules of serial, numpy, matplotlib, math and csv

import serial
import numpy as np
import matplotlib.pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D
import math
import csv

# Definition of number of data in each row as x_size=40
x_size = 40

# Definition of number of data in each column as x_size=40
y_size = 40

# Definition of the size of data
totalData_size = x_size * y_size

# Definition of matrix of zeros in the size of totalData_size.
data = [0] * totalData_size

# Initialize max_data variable to updated later.
max_data = 0

# Definition of empty array of expectedDistance.
expectedDistance = []

# Definition of empty array of the measured servo angles.
servoAngles = []

# Initialize empty arrays of x,y,z scatter data.
x_scatter = []
y_scatter = []
z_scatter = []

# Initialize empty arrays of final x,y,z scatter data.
x_final = []
y_final = []
z_final = []

# Define 'ser' variable as the input from the serial port. 
ser = serial.Serial('/dev/ttyACM2',9600)

# Variable 'fig' makes a figure of plt.
fig = plt.figure()

# Creation of 'ax' figure as sublot in 3d.
ax = fig.add_subplot(111, projection='3d')

# Initializes loop through the totalData_size integer.
for x in range(totalData_size):
	
	# Updates servoAngles array, via appending to the array the float rad value of the two angles in the x and y direction as a tuple.
	servoAngles.append(( float(ser.readline())*math.pi/180.0, float(ser.readline())*math.pi/180.0 ))
	
	# Assigns the float of each serial monitor value as the x_th term of the data array.
	data[x] = float(ser.readline())
	
	# 'if-loop' that sets the max_data 
	if data[x] > max_data:
		max_data = data[x]
		
	# Prints data and servoAngles in rads
	print data[x], servoAngles[x]

# Initializes loop through the totalData_size integer.
for i in range(totalData_size):
	
	# Normalization of data, assigning values between 0 and 1.
	data[i] = data[i] / max_data

# Definition of coefficients a,b,c,d for the approximation equation
a = 372.2
b = -3.962
c = 99.51
d = -0.6113

# Initiates loop through the empty, initially, 'data' array.
for i in data:
	
	# Appends to the expectedDistance array the value of the function of the expected distance
	expectedDistance.append(a * math.exp(b * i) + c * math.exp(d * i))

# Update of the x_scatter, y_scatter and z_scatter array. 
x_scatter = range(totalData_size)
x_scatter = [n/x_size for n in x_scatter]
y_scatter = range(y_size) * x_size

# Use of csv_file variable as a mean to open the .csv file.
csv_file = open("data.csv", "wb")

# Definition of a csv writter.
csv_writer = csv.writer(csv_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

# Initiates loop through totalData_size.
for i in range(totalData_size):
	
	# Csv_writter writes to the csv file.
	csv_writer.writerow([x_scatter[i], y_scatter[i], expectedDistance[i]])

# Prints expectedDistance array.
print expectedDistance

# Initiates 'for-loop' through the totalData_size.
for i in range(totalData_size):
	
	# Filters data less than 100cm.
	if expectedDistance[i] < 100:
		
		# Final update of the final arrays with the data.
		x_final.append(x_scatter[i])
		y_final.append(y_scatter[i])
		z_final.append(expectedDistance[i])


# for i in range(totalData_size):
# 	x_scatter.append(expectedDistance[i] * np.cos(servoAngles[i][0]) * np.sin(servoAngles[i][1]))
# 	y_scatter.append(expectedDistance[i] * np.sin(servoAngles[i][0]) * np.sin(servoAngles[i][1]))
# 	z_scatter.append(expectedDistance[i] * np.cos(servoAngles[i][1]))

# Scatter plot of the final data.
ax.scatter(x_final, y_final, z_final)

# Show the plot figure.
plt.show()
