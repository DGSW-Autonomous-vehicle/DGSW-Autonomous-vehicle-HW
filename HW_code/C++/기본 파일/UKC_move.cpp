
#include <iostream>
#include <wiringPi.h>
#include <softPwm.h>

#define ain1 26
#define ain2 23
#define ena 22

#define bin1 28
#define bin2 29
#define enb 22


using namespace std;

void init_wringPi();

int main(){
    init_wringPi();
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

}
