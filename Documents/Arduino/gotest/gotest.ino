#define PIN_ANALOG_X 0
#define PIN_ANALOG_Y 1

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print("x:");
  Serial.println(analogRead(A0));
  Serial.print("y:");
  Serial.println(analogRead(A1));
  delay(1000);
}
