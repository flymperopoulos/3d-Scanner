#Description of Files#

1. **sensor3D.ino** - Arduino program that sweeps across a 40-degree by 40-degree area and prints data to the serial monitor
2. **calibration.ino** - Arduino program that just prints sensor readings to the serial monitor
3. **grab.py** - Python program that takes in and graphs data from the serial monitor
4. **sensorData.mat** - Matlab matrix with all our calibration data
5. **actual_vs_expected.m** - Matlab code that plots actual distances vs. expected distances (given by our fitted curve)
