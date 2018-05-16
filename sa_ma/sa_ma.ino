// LE - Left Electrode
// RE - Right Electrode
// UE - Upper Electrode
// DE - Down Electrode

long randNumber;

void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() {
  randNumber = random(300);
  Serial.println(randNumber);

  // print a random number from 10 to 19
  randNumber = random(0, 1);
  Serial.println(randNumber);

  delay(50);
}
