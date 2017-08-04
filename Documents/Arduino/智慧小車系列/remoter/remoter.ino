#include <IRremote.h>
#include <IRremoteInt.h>

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
IRsend ir;
int x = 0;
int y = 0;
int xx = 0;
int yy = 0;
int mode = 0;
int last_mode=0;
void setup() {
  // put your setup code here, to run once:
	pinMode(3,OUTPUT);
	Serial.begin(9600);
	Serial.println("begin");
}

void loop() {
  // put your main code here, to run repeatedly:
	x = analogRead(A0);
	y = analogRead(A1);
	if (x>800){
		xx= 1;
	}else if(x<250){
		xx=-1;
	}else{
		xx=0;
	}
	if (y>900){
		yy=10;
	}else if(y<150){
		yy=-10;
	}else{
		yy=0;
	}
	mode=xx+yy;
	switch(mode){
		case 10:	//當為上
			ir.sendNEC(up,32);
			Serial.println("up");
			break;
		case -10:	//當為下
			ir.sendNEC(dw,32);
			Serial.println("down");
			break;
		case 1:		//當為右
			ir.sendNEC(rt,32);
			Serial.println("right");
			break;
		case -1:	//當為左
			ir.sendNEC(lt,32);
			Serial.println("left");
			break;
		case 11:	//當為右上
			ir.sendNEC(ur,32);
			Serial.println("up and right");
			break;
		case 9:		//當為左上
			ir.sendNEC(ul,32);
			Serial.println("up and left");
			break;
		case -9:	//當為右下
			ir.sendNEC(dr,32);
			Serial.println("down and right");
			break;
		case -11:	//當為左下
			ir.sendNEC(dl,32);
			Serial.println("down and left");
			break;
		case 0:		//當為中間
			ir.sendNEC(st,32);
			//Serial.println("stop");
			break;
	}
	
	
}
