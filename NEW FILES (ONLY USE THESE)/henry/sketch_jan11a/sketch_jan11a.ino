int soilMoisturePin = A0; // Connect the soil moisture sensor to analog pin A0
const int relayPin = 8; // Connect the relay to digital pin 8
void setup() {
 Serial.begin(9600); 
 pinMode(soilMoisturePin, INPUT); // Set A0 as an input for soil moisture sensor
 pinMode(relayPin, OUTPUT); // Set digital pin 8 as an output for the relay
}
void loop() {

 int soilMoistureValue = soilMoistureValue + analogRead(soilMoisturePin); // Read soil moisture value from sensor
  soilMoistureValue = soilMoistureValue/100.0; 
  Serial.println(soilMoistureValue); 
 if (soilMoistureValue < 5
 
) {
   digitalWrite(relayPin, HIGH); // Turn on the relay if soil moisture is below 10
 } else {
   digitalWrite(relayPin, LOW); // Turn off the relay otherwise
 }

 delay(1000); // Add a delay to avoid rapid switching, adjust as needed
   if (Serial.available() > 0) {
      char recivedChar = Serial.read();
      if (recivedChar == '1') {
          digitalWrite(8, HIGH);
          delay(2000); 
          digitalWrite(8, LOW);
        }
}

 //Serial.println("relay =" + String(digitalRead(relayPin)) + String(soilMoistureValue)); 
}
