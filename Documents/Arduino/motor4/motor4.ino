#include <Servo.h>
Servo m;
void setup() {
  // put your setup code here, to run once:
  int tim=5000;
  m.attach(9);
  m.write(92);
  for(int i=0;i<3;i++){
    m.write(0);
    delay(tim);
    m.write(180);
    delay(tim);
  }
  m.write(92);
}

void loop() {
  // put your main code here, to run repeatedly:

}
