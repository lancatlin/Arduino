 #include <IRremote.h>
int RECV_PIN = 11;
boolean red=false;
IRrecv re(RECV_PIN);
decode_results results;
#define r1 5
#define r2 6
#define l1 3
#define l2 4

#define st 0xFFFFF00
#define up 0xAABB123
#define dw 0xCCDD234
#define rt 0xEEFF345
#define lt 0xFF00456
#define ur 0xAAEE567
#define ul 0xAAFF678
#define dr 0xCCEE789
#define dl 0xCCFF890
#define b1 0xABCDEF1
#define b2 0xABCDEF2
#define b3 0xABCDEF3
#define b4 0xABCDEF4

void setmotor(int A, int B) {
  if (A > 0) {
    //analogWrite(rs, A);
    analogWrite(r1, A);
    digitalWrite(r2, LOW);
  } else if (A < 0) {
    //analogWrite(rs, abs(A));
    digitalWrite(r1, LOW);
    analogWrite(r2, A);
  } else {
    //analogWrite(rs, 0);
    digitalWrite(r1, LOW);
    digitalWrite(r2, LOW);
  }
  if (B > 0) {
    //analogWrite(ls, B);
    analogWrite(l1, B);
    digitalWrite(l2, LOW);
  } else if (B < 0) {
    //analogWrite(ls, abs(B));
    digitalWrite(l1, LOW);
    analogWrite(l2, B);
  } else {
    //analogWrite(ls, 0);
    digitalWrite(l1, LOW);
    digitalWrite(l2, LOW);
  }
}
void setup() {
  // put your setup codree here, to run once:
  Serial.begin(9600);
  re.blink13(true);
  re.enableIRIn();
  Serial.println("begin");
  for (int i = 2; i < 7; i++) {
    pinMode(i, OUTPUT);
  }
  pinMode(12,OUTPUT);

}

void loop() {
  
    // put your main code here, to run repeatedly:
    if (re.decode(&results)) {
		Serial.println(results.value,HEX);
      switch(results.value){
		case up:   //前進
			Serial.println("up");
			setmotor(150, 150);
			delay(0);    
			break;
        case dw:   //後退
			Serial.println("down");
			setmotor(-150, -150);
			delay(0);
          
			break;
		case rt:   //右轉
			setmotor(-150, 150);
			delay(0);
			break;
        case lt:    //左轉
			setmotor(150, -150);
			delay(0);       
			break;
		case ur:	//右上
			setmotor(0,150);
			break;
		case ul:  	//左上
			setmotor(150,0);
			break;
		case dr:	//右下
			setmotor(0,-150);
			break;
		case dl:	//左下
			setmotor(-150,0);
			break;
        case b1:  //LEDred
			red= !red;
			digitalWrite(12,red);
			break;
        case b2:   //蜂鳴器
			analogWrite(9,200);
			delay(0);
			analogWrite(9,0);
			break;
      default:   //停車
      setmotor(0, 0);
      break;
      }
      delay(0);
      re.resume();
  }

}

