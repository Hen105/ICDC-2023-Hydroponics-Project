int sensorPin = A0;   
int relayPin = 2;     
int sensorValue;      

void setup() {
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW);  
  Serial.begin(9600);  
}

void loop() {
  sensorValue = analogRead(sensorPin);  
  Serial.print("Moisture Level: ");
  Serial.println(sensorValue);
  delay(5000);

  if (sensorValue > 500) {
    digitalWrite(relayPin, HIGH);  
    delay(3000);  
    digitalWrite(relayPin, LOW);  
  }

    
}
