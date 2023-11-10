int sensorPin = A0;   
int sensorValue;     
void setup() {
  Serial.begin(9600);  
}

void loop() {
  sensorValue = analogRead(sensorPin);  
  Serial.print("Moisture Level: ");
  Serial.println(sensorValue);

  delay(1000);  
}
