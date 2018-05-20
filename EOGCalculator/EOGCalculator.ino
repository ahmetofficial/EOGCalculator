// LE - Left Electrode
// RE - Right Electrode
// UE - Upper Electrode
// DE - Down Electrode

const int analogPinRL = A0;
const int analogPinRLReversed = A1;
const int analogPinUD = A2;
const int analogPinUDReversed = A1;

int RL = 0;
int RLReversed = 0;
int RLMain, UDMain;
int UD = 0;
int UDReversed = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  RL = analogRead(analogPinRL);
  RLReversed = analogRead(analogPinRLReversed);
  UD = analogRead(analogPinUD);
  UDReversed = analogRead(analogPinUDReversed);
  
  RLMain=RL-RLReversed;
  UDMain=UD-UDReversed;
  Serial.print(RL);
  Serial.println();
  Serial.flush();
  delay(100);
}
