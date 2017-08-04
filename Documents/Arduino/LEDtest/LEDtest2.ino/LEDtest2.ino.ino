int led = 7;
int in;
void setup() {
  // put your setup code here, to run once:
  pinMode(led,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  in=Serial.read();
  if(in=='R'){
    Serial.println("I see.");
    digitalWrite(led,true);
    delay(1000);
    digitalWrite(led,false);
    delay(1000);
    in=0;
  }
}
