
#include <iostream>
#include <wiringPi.h>
#include <softPwm.h>

//왼쪽 바퀴 핀
#define ain1 26
#define ain2 23

//오른쪽 바퀴 핀
#define bin1 28
#define bin2 29

//왼쪽 바퀴 PWM핀
#define ena 22

//오른쪽 바퀴 PWM핀
#define enb 25

using namespace std;

// 속도값 변수
char ENA = 100;
char ENB = 100;

//////////////// 자치차량 함수 선언부 /////////////////////////

// 초기화 함수
void init_wringPi();

// 움직임제어 함수 
void forward();
void stop();
void back();
void left();
void right();

//속도값 제어함수
void setPWM(int a,int b); 
void setPWMA(int a); // 왼쪽 바퀴
void setPWMB(int a); // 오른쪽 바퀴

//////////////////////////////////////////////////////////////


//// 우리의 개쩌는 main 함수님 ////
int main(){

    init_wringPi(); //초기화 코드

    while(1) { 
        cout << "forward" << endl;
        forward();
        delay(1000);

        cout << "back" << endl;
        back();
        delay(1000);

        
        cout << "right" << endl;
        right();
        delay(1000);

        
        cout << "left" << endl;
        left();
        delay(1000);

        
        cout << "stop" << endl;
        stop();
        delay(1000);

        
    }
}

/////////////////// 초기화 함수 /////////////////

void init_wringPi(){
    if(wiringPiSetup() == -1){
        cout << "WirginPi Setup Error" << endl;   
        return;
    }

    pinMode(ain1,OUTPUT);
    pinMode(ain2,OUTPUT);
    pinMode(ena,OUTPUT);

    pinMode(bin1,OUTPUT);
    pinMode(bin2,OUTPUT);
    pinMode(enb,OUTPUT);

    softPwmCreate(ena,0,255);
    softPwmCreate(enb,0,255);
}


//////////////////// 움직임 제어함수 /////////////

void forward(){
   softPwmWrite(ena,ENA);
   softPwmWrite(enb,ENB);

   digitalWrite(ain1,LOW);
   digitalWrite(ain2,HIGH);
   digitalWrite(bin1,LOW);
   digitalWrite(bin2,HIGH);
}

void stop(){
   softPwmWrite(ena,0);
   softPwmWrite(enb,0);

   digitalWrite(ain1,LOW);
   digitalWrite(ain2,LOW);
   digitalWrite(bin1,LOW);
   digitalWrite(bin2,LOW);
}

void back(){
    softPwmWrite(ena,50);
    softPwmWrite(enb,50);

    digitalWrite(ain1,HIGH);
    digitalWrite(ain2,LOW);
    digitalWrite(bin1,HIGH);
    digitalWrite(bin2,LOW);
}

void right(){
    softPwmWrite(ena,30);
    softPwmWrite(enb,30);

    digitalWrite(ain1,LOW);
    digitalWrite(ain2,HIGH);
    digitalWrite(bin1,HIGH);
    digitalWrite(bin2,LOW);
}

void left(){
    softPwmWrite(ena,30);
    softPwmWrite(enb,30);

    digitalWrite(ain1,HIGH);
    digitalWrite(ain2,LOW);
    digitalWrite(bin1,LOW);
    digitalWrite(bin2,HIGH);
}

/////////////// 속도값 제어 함수 ///////////////////

void setPWM(int a, int b){
    setPWMA(a);
    setPWMB(b);
}

void setPWMA(int a){
    ENA = a;
}

void setPWMB(int a){
    ENB = a;
}
