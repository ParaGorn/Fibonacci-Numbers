#include <stdio.h>

int main() {
	int x;
//	sscanf( "%d", &x );
	scanf( "%d", &x );
	printf( "%d\n", (x^((~((x>>31)&1))+1)) + ((x>>31)&1) );
	return 0;
}

