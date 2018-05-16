const int pin = A0;
int value;
void setup() {
  Serial.begin(9600);
}

void loop() {
  value = analogRead(pin);
  if(value>0){
    Serial.print(1);
    Serial.println();
    Serial.flush();
    delay(100);
  }else{
    Serial.print(0);
    Serial.println();
    Serial.flush();
    delay(50);
  }
}
