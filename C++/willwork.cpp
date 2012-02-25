#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>
#include <string>
using namespace std;


int main(int argc, char** argv)
{
	int x;
	x = atoi(argv[1]);
	cout << (x>>31) << endl;
	cout << ((x>>31)<<31) << endl;
	cout << x << endl;
	x = (x^((x>>31)<<31));
	printf("%d\n", x);
	return 0;
}


