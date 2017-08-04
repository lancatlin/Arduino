#include <Arduino.h>
#include <Wire.h>
#include <SoftwareSerial.h>


double angle_rad = PI/180.0;
double angle_deg = 180.0/PI;
double result;



void setup(){
    int result;
    Serial.begin(9600);
    pinMode(6,INPUT);
    pinMode(5,INPUT);
}

void loop(){
    
    if(digitalRead(6)==HIGH){
        result=0;
        for(int i=0;i<8;++i)
        {
            /*int y=1;
            for (int j=1;j<__i__;j++){
              y=y*2;
            }
            result = result+digitalRead(5)*y;
            */
            Serial.print(digitalRead(5));
            delay(100);
        }
        Serial.println();
    }
    
    _loop();
}

void _delay(float seconds){
    long endTime = millis() + seconds * 1000;
    while(millis() < endTime)_loop();
}

void _loop(){
    
}

