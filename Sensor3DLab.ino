#include <Servo.h> 
 
Servo servoHorizontal;  // create servo object to control a servo 
Servo servoVertical;
long previousMillis = 0;        // will store last time LED was updated

int pos = 0;    // variable to store the servo position 
int interval = 100; 
int data;
const int sensorPin = A1;
int counter = 0;

float sensorVoltage;
 
void setup() 
{
  pinMode(sensorPin,INPUT);  
  servoHorizontal.attach(9);  // attaches the servo on pin 9 to the servo object 
  servoVertical.attach(13);  
  Serial.begin(9600);
} 
 
void loop() { 
   unsigned long currentMillis = millis();
   data = analogRead(sensorPin);
   sensorVoltage = data * (5.0/1023.0);

   for (int currentXPos = 0; currentXPos < 80; currentXPos++){
     servoHorizontal.write(currentXPos);
     for (int currentYPos = 80; currentYPos < 100; currentYPos++){
       servoVertical.write(currentYPos);
       if (currentMillis - previousMillis>interval){
         previousMillis = currentMillis;
         Serial.println(sensorVoltage);
       }       
     }
       if (currentMillis - previousMillis>interval){
         previousMillis = currentMillis;
         data = analogRead(sensorPin);
         Serial.end();
       }    
   }
}

void readData(){
  
}
