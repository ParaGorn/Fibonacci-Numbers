import os, glob, msvcrt, datetime

# commas for name, not for number
# do NOT overwrite

x = -1
for fn in glob.glob("*.fib"):
    y = int(fn[:-4])
    if y > x:
        x = y

num = 1
a = 0
b = 1
c = 0


if x > 0:
    fn1 = str(x) + ".fib"
    fn2 = str(x-1) + ".fib"
    print ("Opening..." + fn1 + " and " + fn2)
    FILE1 = open(fn1, "r")
    FILE2 = open(fn2, "r")
    b = int(FILE1.read())
    a = int(FILE2.read())
    FILE1.close()
    FILE2.close()
    num = x

done = False

while not done:
    num += 1
    c = b + a
    a = b
    b = c

    print (num)

    if num%100000 == 0:
        now = datetime.datetime.now()
        if now.strftime("%A") == "Monday" or now.strftime("%A") == "Wednesday":
            if now.hour == 14 and now.minute >= 0:
                done = True
        elif now.strftime("%A") == "Friday":
            if now.hour == 14 and now.minute >= 0:
                done = True

    if num%1000000 == 0:
            fn = str(num) + ".fib"
            FILE = open(fn, "w")
            FILE.write(str(c))
            FILE.close()

            fn = str(num-1) + ".fib"
            FILE = open(fn, "w")
            FILE.write(str(a))
            FILE.close()
    
    if msvcrt.kbhit():
            temp = msvcrt.getch()

            if temp == b'q':
                done = True
            else:
                fn = str(num) + ".fib"
                FILE = open(fn, "w")
                FILE.write(str(c))
                FILE.close()

                fn = str(num-1) + ".fib"
                FILE = open(fn, "w")
                FILE.write(str(a))
                FILE.close()
        

print ("You got to the %d fibonacci number!" % num)
fn = str(num) + ".fib"
FILE = open(fn, "w")
FILE.write(str(c))
FILE.close()

fn = str(num-1) + ".fib"
FILE = open(fn, "w")
FILE.write(str(a))
FILE.close()
