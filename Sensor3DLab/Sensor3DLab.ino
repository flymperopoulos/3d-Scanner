#include <Servo.h> 
 
Servo servoHorizontal;  // create servo object to control a servo 
Servo servoVertical;
const int sensorPin = A1;
const int servoPinX = 13;
const int servoPinY = 9;

long time = 0;          // will store last time LED was updated
int sensingInterval = 100; 
int counter;
float data_sum;
 
void setup() 
{
  pinMode(sensorPin, INPUT);  
  servoHorizontal.attach(servoPinX);  // attaches the servo on pin 9 to the servo object 
  servoVertical.attach(servoPinY);  
  
  Serial.begin(9600);
} 
 
void loop() {
  servoHorizontal.write(50);
  servoVertical.write(70);
  delay(2000);
  time = millis();
  
   for (int currentXPos = 50; currentXPos < 90; currentXPos++){
     servoHorizontal.write(currentXPos);
     for (int currentYPos = 70; currentYPos < 110; currentYPos++){
       servoVertical.write(currentYPos);
       counter = 1;
       data_sum = 0.0;
       while (millis() - time < sensingInterval) {
         data_sum += analogRead(sensorPin) * 5.0/1023.0;
         counter++;
       }
       time = millis();
       Serial.println(data_sum / counter);
     }
   }
  while (1){}
}
