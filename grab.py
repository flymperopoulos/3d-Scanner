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

# yData = [0]*50
# ax1=plt.axes()  
 
# # make plot
# line, = plt.plot(yData)
# plt.ylim([10,40]) # set the y-range to 10 to 40

# # data collection
# while True:
# 	data = ser.readline().rstrip()

# 	if len(data.split('.'))==3:
# 		yMin = float(min(yData))-10
# 		yMax = floa t(min(yData))+10
# 		plt.ylim([yMin,yMax])
# 		yData.append(data)
# 		del yData[0]
# 		line.set_xData(np.arange(len(yData)))
#         line.set_yData(yData)  # update the data
#         plt.draw() # update the plot



#     #newArray.append(var)
#     #print newArray[len(newArray)-1]
