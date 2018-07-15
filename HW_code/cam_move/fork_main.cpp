//#include "Unreal_Liner.h"
//#include "TL.hpp"
//#include "UKC_move_class.h"


#include <iostream>
#include <unistd.h>
#include <thread>

using namespace std;

int flag = -1;

void Liner_ando();
void Move_UKC();

int main(int argc, char const *argv[])
{
    thread Liner_th(&Liner_ando);
    Liner_th.join();

    Move_UKC();
    
    return 0;
}

void Liner_ando(){
    while(1){
        cout << "analog" << endl;
    }
    /*
    Liner Line;
    Line.startLiner();
    return;
    */
}

void Move_UKC(){
    while(1){
        cout << "digital" <<endl;
    }
    
    /*
    UKC_move Move;

    while(1){

        switch (flag){
            case -1: // 정지
                Move.stop();
                break;

            case 0: //직진
                Move.forward();
                break;

            case 1: // 오른쪽
                Move.right();
                break;

            case 2: // 좌파
                Move.left();
                break;
            default:
                cout << "배애애에에" << endl;
                Move.stop();
                break;
        }
        delay(80);

    }    
    return;
    */
}
