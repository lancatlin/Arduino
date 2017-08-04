#include <dht.h>
#define dht_pin 3

#define d A0
#define DS 8
#define SH_CP 9
#define ST_CP 10

int number[][8] = {
	{1,1,1,1,1,1,0,0}, //0
	{0,1,1,0,0,0,0,0}, //1
	{1,1,0,1,1,0,1,0}, //2
	{1,1,1,1,0,0,1,0}, //3
	{0,1,1,0,0,1,1,0}, //4
	{1,0,1,1,0,1,1,0}, //5
	{1,0,1,1,1,1,1,0}, //6
	{1,1,1,0,0,0,0,0}, //7
	{1,1,1,1,1,1,1,0}, //8
	{1,1,1,1,1,1,0,0}, //9
	{0,0,0,0,0,0,0,0}, //none
};
void set_number(int info,int pin){
	digitalWrite(ST_CP,LOW);
	for (int i = 0;i<=7;i++){
		digitalWrite(DS,number[info][7-i]);
		digitalWrite(SH_CP,HIGH);
		digitalWrite(SH_CP,LOW);
		}
	digitalWrite(ST_CP,HIGH);
	for(int i =4;i<=7;i++){
		if (i!=pin+3){
			digitalWrite(i,HIGH);
		}else{
			digitalWrite(i,LOW);
		}
	}
	delay(5);
	digitalWrite(ST_CP,LOW);
}
void clean(){
	for (int j=4;j<=7;j++){
		set_number(10,j);
	}
}
int cut(int num,int a){
	int b = num/pow(10,a);
	return b%10;
	}
void setup() {
  // put your setup code here, to run once:
	pinMode(2,INPUT);
	pinMode(11,INPUT);
	digitalWrite(2,HIGH);
	digitalWrite(11,HIGH);
	Serial.begin(9600);
	delay(300);
	Serial.println("begin");
	delay(700);
	for (int i = 4;i<=10;i++){
		pinMode(i,OUTPUT);
	}
}

void loop() {
  // put your main code here, to run repeatedly:
	int val=analogRead(d);
	for (int i=0;i<=20;i++){
		set_number(cut(val,0),1);
		set_number(cut(val,1),2);
		set_number(cut(val,2),3);
		set_number(cut(val,3),4);
	}
}