
#include <iostream>
#include <wiringPi.h>
#include <softPwm.h>

#define ain1 26
#define ain2 23
#define ena 22

#define bin1 28
#define bin2 29
#define enb 22

char ENA = 100;
char ENB = 100;

using namespace std;

void init_wringPi();

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

int main(){
    init_wringPi();
    while(1) {
        forword();
    }
}

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

