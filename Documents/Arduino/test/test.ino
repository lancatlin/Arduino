double red=13;
double blue=12;
double button=2;
double buzzer=9;
void W(int pin,int mode){
  digitalWrite(pin,mode);
}
void setup() {
  // put your setup code here, to run once:
  pinMode(red,OUTPUT);
  pinMode(blue,OUTPUT);
  pinMode(button,INPUT);
  pinMode(buzzer,OUTPUT);
  W(button,HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(button)==LOW){
    analogWrite(buzzer,random(1,10)*15+50);
    W(red,HIGH);
    delay(100);
    W(red,LOW);
    W(blue,HIGH);
    delay(100);
    W(blue,LOW);
  }else{
    analogWrite(buzzer,0);
  }
}
