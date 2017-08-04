double angle_rad = PI/180.0;
double angle_deg = 180.0/PI;
long x;
double i;



void setup(){
    x = 00001101;
    pinMode(5,OUTPUT);
    pinMode(6,OUTPUT);
    pinMode(2,INPUT);
    digitalWrite(5,0);
    digitalWrite(6,0);    
}

void loop(){
    
    digitalWrite(6,HIGH);
        digitalWrite(5,HIGH);
        delay(100);
        digitalWrite(5,LOW);
        delay(100);
    
    _loop();
}

void _delay(float seconds){
    long endTime = millis() + seconds * 1000;
    while(millis() < endTime)_loop();
}

void _loop(){
    
}

