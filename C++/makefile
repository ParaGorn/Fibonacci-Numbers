CC = g++
CFLAGS = `pkg-config --libs cln` `pkg-config --cflags cln`
#CFLAGS = -g -Wall

all: 0fib1 0fib2 0fib3 0bitTwiddling

0fib3:
	$(CC) $(CFLAGS) -o 0fib3 fib3.cpp

0fib2:
	$(CC) $(CFLAGS) -o 0fib2 fib2.cpp

0fib1:
	$(CC) $(CFLAGS) -o 0fib1 fib1.cpp

0bitTwiddling:
	$(CC) -o 0bitTwiddling bitTwiddling.cpp
