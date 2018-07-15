#include "UKC_move_class.h"

int main(){
	UKC_move Move;

	Move.init_wringPi();

	char input;

	cout << "'h' key is exit()"<< endl;

	while(1){
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

			case 'h':
				Move.stop();
				cout << "Bye" << endl;	
				return 0;

		}
	}

	return 0;

}
