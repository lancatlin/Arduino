byte in = A0;
byte first;
byte mode;
void setup() {
  Serial.begin(9600);
  first = (analogRead(in));
  // put your setup code here, to run once:
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
}

void loop() {
  mode = (analogRead(in) - first);
  if(mode>10){
    mode=0;
  }
  delay(500);
  //mode = Serial.read();
  //Serial.println(mode);
  
  Serial.println();
  Serial.println(mode);
  for (int i = 6; i <= 9; i++) {
    if ((mode + 6) > i) {
      digitalWrite(i, HIGH);
      Serial.print(i);
    } else {
      digitalWrite(i, LOW);
    }
  }
  // put your main code here, to run repeatedly:

}

