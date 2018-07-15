#include "UKC_move_class.h"

int main(){
	UKC_move Move;

	Move.init_wringPi();

	char input;

	cout << "'h' key is exit()"<< endl;

	while(1){
		if(kbhit()){ //키가 입력이 될 경우
			input = getch();

			switch(input){
				case 'w':
					Move.forward();
					break;

				case 'a':
					Move.left();
					break;

				case 's':
					Move.back();
					break;

				case 'd':
					Move.right();
					break;
				case ' ':
					Move.stop();
					break;

			}
		}
		else{  // 키입력이 없을 경우
			Move.stop();
		}
	}

	return 0;
	
}
