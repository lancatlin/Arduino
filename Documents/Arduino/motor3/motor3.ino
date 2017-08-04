#include<Stepper.h>
#define STEPS 48
Stepper motor(STEPS,8,9,10,11);
    int pre=0;
    int val;


void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
    motor.setSpeed(100);
    val=1;
}

void loop() {
  // put your main code here, to run repeatedly:
  
      //val=Serial.read();
      motor.step(val);
      //delay(1000);
      Serial.println(val);
}
