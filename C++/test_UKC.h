#include <iostream>
#include <wiringPi.h>
#include <softPwm.h>
#include <stdlib.h>

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

#define DR
#define DL

using namespace std;

class UKC_move{

    private:

        // 속도값 변수
        char ENA = 120;
        char ENB = 120;

    public:

        void init_wringPi();  // 초기화 함수

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

        void init_Infared();
        void Infared();
};

/////////////////// 초기화 함수 /////////////////
void UKC_move::init_wringPi(){
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

void UKC_move::forward(){
   softPwmWrite(ena,ENA);
   softPwmWrite(enb,ENB);

   digitalWrite(ain1,LOW);
   digitalWrite(ain2,HIGH);
   digitalWrite(bin1,LOW);
   digitalWrite(bin2,HIGH);
}

void UKC_move::stop(){
   softPwmWrite(ena,0);
   softPwmWrite(enb,0);

   digitalWrite(ain1,LOW);
   digitalWrite(ain2,LOW);
   digitalWrite(bin1,LOW);
   digitalWrite(bin2,LOW);
}

void UKC_move::back(){
    softPwmWrite(ena,ENA);
    softPwmWrite(enb,ENB);

    digitalWrite(ain1,HIGH);
    digitalWrite(ain2,LOW);
    digitalWrite(bin1,HIGH);
    digitalWrite(bin2,LOW);
}

void UKC_move::right(){
    softPwmWrite(ena,45);
    softPwmWrite(enb,45);

    digitalWrite(ain1,LOW);
    digitalWrite(ain2,HIGH);
    digitalWrite(bin1,HIGH);
    digitalWrite(bin2,LOW);
}

void UKC_move::left(){
    softPwmWrite(ena,45);
    softPwmWrite(enb,45);

    digitalWrite(ain1,HIGH);
    digitalWrite(ain2,LOW);
    digitalWrite(bin1,LOW);
    digitalWrite(bin2,HIGH);
}

void init_Infrared(){
    
}

void Infrared(){

}

/////////////// 속도값 제어 함수 ///////////////////

void UKC_move::setPWM(int a, int b){
    setPWMA(a);
    setPWMB(b);
}

void UKC_move::setPWMA(int a){
    ENA = a;
}

void UKC_move::setPWMB(int a){
    ENB = a;
}
