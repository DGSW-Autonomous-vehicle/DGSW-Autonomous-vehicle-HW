#include "Unreal_Liner.h"
#include "TL.hpp"
#include "UKC_move_class.h"

#include <thread>

int flag = -1;

void Liner_ando();
void Move_UKC();


Liner Line;
UKC_move Move;

int main(int argc, char const *argv[])
{
    Move.init_wringPi();
    
    thread Liner_th(&Liner_ando);
    thread Move_th(&Move_UKC);

    Move_th.join();
    Liner_th.join();
    
    return 0;
}

void Liner_ando(){
    cout <<"Liner 진입"<< endl;    
    Line.startLiner();
    return;
}

void Move_UKC(){
    cout << "Move 진입" << endl;
    while(1){
        flag = Line.flag;
        cout << "flag = " << flag << endl;
        
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
            case 3:
                Move.forward(40,20);
                break;
            case 4:
                Move.forward(20,40);
                break;

            default:
                cout << "배애애에에" << endl;
                Move.stop();
                return;
        }
        delay(20);

    }    
    return;
}
