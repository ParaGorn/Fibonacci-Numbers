#!/usr/bin/python
from sys import *
import os


def main():
    if int(argv[1]) > 1:
        a = 0
        b = 1
        for i in range(1,int(argv[1])):
            c = a + b
            a = b
            b = c
            stdout.write("%s - %d%% done\r" % (group(i), float(i)/float(argv[1])*100))
            stdout.flush()

        if c < 2**100000:
            stdout.write("                                                          \r")
            stdout.flush()
            print "fib(%d): %d" %(int(argv[1]), c)
        else:
            out = open ("fib_of_" + argv[1] + '.out', 'w')
            out.write(group(c) + '\n')
            out.close()

    elif int(argv[1]) == 1:
        print "fib(%d): 1" %int(argv[1])
    elif int(argv[1]) == 0:
        print "fib(%d): 0" %int(argv[1])
    else:
        print "Invalid input. Must be a positive integer"


def group(number):
    s = '%d' % number
    groups = []
    while s and s[-1].isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    return s + ','.join(reversed(groups))



main()
