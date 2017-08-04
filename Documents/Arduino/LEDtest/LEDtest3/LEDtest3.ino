byte one=7;
byte two=8;
byte three=9;
byte in=3;
boolean mode=true;
void setup() {
  // put your setup code here, to run once:
  pinMode(one,OUTPUT);
  pinMode(two,OUTPUT);
  pinMode(three,OUTPUT);
  pinMode(in,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(in)==LOW){
    digitalWrite(one,mode);
    digitalWrite(two,!mode);
    digitalWrite(three,LOW);
    delay(150);
    mode = !mode;
  }else{
    digitalWrite(one,LOW);
    digitalWrite(two,LOW);
    digitalWrite(three,HIGH);
    delay(50);
  }
}
