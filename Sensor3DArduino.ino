// Includes the Servo.h library.
#include <Servo.h> 

// Creation of servo objects to control the servos in vertical and horizontal directions.
Servo servoHorizontal;   
Servo servoVertical;

// Definition of servos' and sensor's pin.
const int sensorPin = A1;
const int servoPinX = 13;
const int servoPinY = 9;

// Stores last time LED was updated.
long time = 0;    

// Interval between events.
int sensingInterval = 120; 

// Initializes counter.
int counter;
float data_sum;

// Definition of servo angles.
int servoAngleX;
int servoAngleY;
 
void setup() 
{
  // Definition of sensor input pin.
  pinMode(sensorPin, INPUT);  
  
  // Attaches the servos on pin 9 and 13 to the servo objects.
  servoHorizontal.attach(servoPinX);  
  servoVertical.attach(servoPinY);  
  
  // Opens serial port, sets data rate to 9600 bps
  Serial.begin(9600);
} 
 
// Initializes the loop() method.
void loop() {
  
  // Writes positions of Horizontal and Vertical servos.
  servoHorizontal.write(50);
  servoVertical.write(70);
  
  // Declares delay.
  delay(2000);
  
  // Assign values to servo angles.
  servoAngleX = -20;
  servoAngleY = -20;
  
   // External "for-loop" for horizontal servo sweep. 
   for (int currentXPos = 50; currentXPos < 90; currentXPos++){
     
     // Writes horizontal servo position.
     servoHorizontal.write(currentXPos);
     
     // Writes vertical servo position.
     servoVertical.write(70);
     // Declaration of delay and time variable.
     delay(200);
     time = millis();
     
     // Internal "for-loop" for verticak servo sweep.
     for (int currentYPos = 70; currentYPos < 110; currentYPos++){
       
       // Writes position of vertical servo
       servoVertical.write(currentYPos);
       
       // Assigns counter to integer 1.
       counter = 1;
       
       // Initializes data_sum variable to zero.
       data_sum = 0.0;
       
       // Prints angle measurements on both planes.
       Serial.println(servoAngleX);
       Serial.println(servoAngleY);
       
       // Increments vertical servo angle.
       servoAngleY++;
       
       // while loop without delay that checks difference between current and previous time data were read from the sensorPin
       while (millis() - time < sensingInterval) {
         
         // Updates data_sum variable, based on analogRead(sensorPin).
         data_sum += analogRead(sensorPin) * 5.0/1023.0;
         
         // Increments counter.
         counter++;
       }
       // Returns the number of milliseconds since the Arduino began running the current program.
       time = millis();
       
       // Prints the average value of the data collected.
       Serial.println(data_sum / counter);
     }
     
     // Increments horizontal angle.
     servoAngleX++;
     
     // Definition of vertical angle to -20.
     servoAngleY = -20;
   }
   
   // "While-loop" that stops program from servos moving.
   while (1){}
}
