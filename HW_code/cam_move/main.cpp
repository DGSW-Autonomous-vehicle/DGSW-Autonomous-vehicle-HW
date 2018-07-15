#include "Unreal_Liner.h"
#include "TL.hpp"
#include "UKC_move_class.h"

#include <unistd.h>

int main(int argc, char const *argv[])
{
    pid_t pid;

    pid = fork();

    char flag;

    if(pid == 0){ // Liner 프로세스 실행
        Liner Line;
        Line.startLiner();
        a = Line.flag;
    }else{
        UKC_move Move;
    
        while(1){

            cout << "flag = " << a << endl;

            switch (a){
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
        }

        delay(30);

    }    
    return 0;
}
