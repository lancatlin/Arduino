#include <Stepper.h>
Stepper Left(300, 15, 4, 12, 17 );
Stepper Right(300, 15, 12, 4, 17);
byte red = 10;
byte green = 11;
void setup() {
  // put your setup code here, to run once:
  Left.setSpeed(150);
  Right.setSpeed(150);
  pinMode(5, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(2, INPUT);
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (!digitalRead(2)) {}
  while (digitalRead(2)) {}
  digitalWrite(red, HIGH);
  digitalWrite(green, HIGH);
  while (!digitalRead(2)) {
    Left.step(100);
  }
  digitalWrite(red, LOW);
  digitalWrite(green, LOW);
  while (digitalRead(2)) {}
}
