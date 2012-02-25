import msvcrt
import os

while 1:
    if msvcrt.kbhit():
        temp = msvcrt.getch()
        #print ("You pressed %s", % temp)
        print ("blarg" + str(temp))
