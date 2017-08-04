int led=13;
int val;
int high=0;
int low=1023;
int sound;
void setup() {
  // put your setup code here, to run once:
  pinMode(led,OUTPUT);
  pinMode(9,OUTPUT);
  digitalWrite(led,HIGH);

  while(millis()<5000){
    val=analogRead(A0);
    if (val > high){
      high=val;
    }
    if (val<low){
      low=val;
    }
  }
  digitalWrite(led,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  val=analogRead(A0);
  sound=map(val,low,high,0,255);
  analogWrite(9,sound);
  delay(50);
  
}
