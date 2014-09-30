#include <Servo.h> 

Servo servoHorizontal;   
Servo servoVertical;

const int sensorPin = A1;
const int servoPinX = 13;
const int servoPinY = 9;

// Stores the time to implement delays
long time = 0;    

// Time interval between each sensor reading
int sensingInterval = 120; 

int counter;
float data_sum;
int servoAngleX;
int servoAngleY;
 
void setup() 
{
  pinMode(sensorPin, INPUT);  
  
  servoHorizontal.attach(servoPinX);  
  servoVertical.attach(servoPinY);  
  
  Serial.begin(9600);
} 
 
// Initializes the loop() method.
void loop() {
  
  // Initializes the servo positions
  servoHorizontal.write(50);
  servoVertical.write(70);
  
  delay(2000);
  
  // Keeps track of servo angles to print to the serial
  servoAngleX = -20;
  servoAngleY = -20;
  
  // Sweeps through the data
  for (int currentXPos = 50; currentXPos < 90; currentXPos++){
    servoHorizontal.write(currentXPos);
    servoVertical.write(70); // Resets the vertical servo
    
    // Declaration of delay and time variable.
    delay(200);
    time = millis();
    
    // Vertical sweep
    for (int currentYPos = 70; currentYPos < 110; currentYPos++){
      servoVertical.write(currentYPos);
      
      // Prints the servo angles to the serial
      Serial.println(servoAngleX);
      Serial.println(servoAngleY);
      servoAngleY++;
      
      // Averages the data collected over the sensingInterval
      counter = 1;
      data_sum = 0.0;
      
      while (millis() - time < sensingInterval) {
        counter++;
        data_sum += analogRead(sensorPin) * 5.0/1023.0;
      }
      
      time = millis();

      // Prints the average value of the data collected
      Serial.println(data_sum / counter);
    }
    
    servoAngleX++;
    servoAngleY = -20;
  }
  
  // Halts everything when the scan is done
  while (1){}
}
