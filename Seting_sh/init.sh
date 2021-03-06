#!/bin/sh

echo "자치차량 init 스크립트"

echo "부저 소리 제거 프로그램 설정중..."
./../HW_EXE/Buzzer_stop
cp seting.txt /etc/rc.local

echo "vim 설정 중..."

git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

vim +PluginInstall +aqll

echo "getch() 함수 라이브러리 설치"

sudo apt-get update
sudo apt-get install ncureses-dev

echo "wirginPi 설치"
git clone git://git.drogon.net/wiringPi
./wirginPi/build

