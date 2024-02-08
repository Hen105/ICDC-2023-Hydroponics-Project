#define SensorPin A0 
int sensorValue = 0; 
void setup() { 
   Serial.begin(9600); 
} 
void loop() { 
 { 
   sensorValue = sensorValue + analogRead(SensorPin); 
   delay(1);   
 } 
 sensorValue = sensorValue/100.0; 
 Serial.println(sensorValue); 
 delay(1000); 
}
 
