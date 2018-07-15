#include "UKC_move_class.h"

int main(){
	UKC_move Move;

	Move.init_wringPi();

	cout << "Test 시작" << endl;
	Move.forward();

	delay(1000);
	Move.stop();

	cout << "성공적" << endl;

	return 0;
	
}
