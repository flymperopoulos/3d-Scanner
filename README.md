#3D Scanner Repo Description#

1. **sensor3D.ino** - Arduino program that sweeps across a 40-degree by 40-degree area and prints data to the serial monitor.
2. **data.csv** - Csv file with the data collected from scanning the area with the Arduino.
3. **grab.py** - Python program that takes in and graphs data as a scatter plot from the serial monitor
4. **sensorData.mat** - Matlab matrix with all our calibration data
5. **actual_vs_expected.m** - Matlab code that plots actual distances vs. expected distances (given by our fitted curve)
6. **examplePictures** - Resulting pictures of the scan.
