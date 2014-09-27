import serial

newArray = []
ser = serial.Serial('/dev/tty.usbmodemfd121',9600)

while True:
    var = ser.readline()
    newArray.append(var)
    print newArray