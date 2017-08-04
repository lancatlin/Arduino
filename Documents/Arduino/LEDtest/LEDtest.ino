
int Red = 10;
int Green = 11;
int Left = 8;
int Right = 7;
int sound = 9;
int button = 2;
void setup() {
  // put your setup code here, to run once:
  pinMode(Red, OUTPUT);
  pinMode(sound,OUTPUT);
  pinMode(button, INPUT);
  pinMode(Left, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (!digitalRead(button)) {
  }
  digitalWrite(Red, HIGH);
  digitalWrite(Green, HIGH);
  tone(sound,200);
  while (digitalRead(button)) {
  }
  digitalWrite(Red, LOW);
  digitalWrite(Green, LOW);
  noTone(sound);
}
