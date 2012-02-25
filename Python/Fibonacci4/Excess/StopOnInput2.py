import msvcrt
import os

# save progress every 1mill numbas and on exit
# commas for name, not for number
# find largest filename (by number) in current direc.
# do NOT overwrite

num = 1
done = False

a = 0
b = 1
c = 0

while not done:
    num += 1
    c = b + a
    a = b
    b = c
    
    print (num)
    #if num == 100:
        #done = True
    if msvcrt.kbhit():
        done = True
        #temp = msvcrt.getch()
        #if temp == b'q':
            #print ("you pressed", chr(temp), "so now i will quit")
            #done = True
        #else:
            #fn = str(num) + ".txt"
            #FILE = open(fn, "w")
            #FILE.write(chr(c))

            #fn = str(num-1) + ".txt"
            #FILE = open(fn, "w")
            #FILE.write(str(a))
            #FILE.close()

print ("You got to the %d fibonacci number!" % num)
fn = str(num) + ".fib"
FILE = open(fn, "w")
FILE.write(str(c))
FILE.close()

fn = str(num-1) + ".fib"
FILE = open(fn, "w")
FILE.write(str(a))
FILE.close()
input()
