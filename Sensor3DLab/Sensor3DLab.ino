#include <Servo.h> 
 
Servo servoHorizontal;  // create servo object to control a servo 
Servo servoVertical;
long previousMillis = 0;        // will store last time LED was updated

int pos = 0;    // variable to store the servo position 
int interval = 80; 
int data;
const int sensorPin = A1;
int counter;
float data_sum;

float sensorVoltage;
 
void setup() 
{
  pinMode(sensorPin,INPUT);  
  servoHorizontal.attach(13);  // attaches the servo on pin 9 to the servo object 
  servoVertical.attach(9);  
  Serial.begin(9600);
} 
 
void loop() { 
//   data = analogRead(sensorPin);
//   sensorVoltage = data * (5.0/1023.0);

  servoHorizontal.write(70);
  servoVertical.write(70);
  delay(2000);
  previousMillis = millis();
  
   for (int currentXPos = 65; currentXPos < 95; currentXPos++){
     servoHorizontal.write(currentXPos);
     for (int currentYPos = 70; currentYPos < 100; currentYPos++){
       servoVertical.write(currentYPos);
       counter = 1;
       data_sum = 0.0;
       while (millis() - previousMillis < interval) {
         data_sum += analogRead(sensorPin) * 5.0/1023.0;
         counter++;
       }
       previousMillis = millis();
       Serial.println(data_sum / counter);
     }
   }
  while (1){}
}
