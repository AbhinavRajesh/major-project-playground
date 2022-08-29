#!/bin/bash

echo -e "\e[34m=====Server Compiling...====="
g++ -I /usr/include/boost -pthread source/server.cc -o server.out

echo -e "=====Server compiled successfully====="

echo -e "=====Running server=====]\033[0;92m"
./server.out
