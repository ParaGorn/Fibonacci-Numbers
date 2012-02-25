#include <cln/integer.h>
#include <cln/real.h>
#include <stdio.h>
#include <cln/io.h>
#include <cln/integer_io.h>
using namespace cln;
using namespace std;

const cl_I fibonacci (int n);
int main(int argc, char** argv) {
	//std::cout << fibonacci(10) << endl;
	//fprintdecimal(fibonacci(10));
	//cout << fibonacci(10) << endl;
	cl_I x;
	x = fibonacci(atoi(argv[1]));
	cout << x << endl;
	return 0;
}

// Returns F_n, computed as the nearest integer to
// ((1+sqrt(5))/2)^n/sqrt(5). Assume n>=0.
const cl_I fibonacci (int n)
{
	// Need a precision of ((1+sqrt(5))/2)^-n.
	float_format_t prec = float_format((int)(0.208987641*n+5));
	cl_R sqrt5 = sqrt(cl_float(5,prec));
	cl_R phi = (1+sqrt5)/2;
	return round1( expt(phi,n)/sqrt5 );
}
