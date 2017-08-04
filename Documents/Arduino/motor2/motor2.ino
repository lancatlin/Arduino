#include <Servo.h>
Servo go;
int val;
void setup() {
  // put your setup code here, to run once:
  go.attach(9);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  val = random(20, 278);
  go.write(val);
  Serial.println(val);
  delay(2000);
}

