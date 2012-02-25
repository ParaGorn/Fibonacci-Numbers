import os, glob


def solution():
    x = 0
    for fn in glob.glob("*.fib"):
        x = int(fn[:-4])
        #y = int(fn[:-4])
        #if y > x:
            #x = y
        #print (fn[:-4])
    #print (x)
    if not x > 0:
        print ("eh")

solution()

"""
os.startfile(fn)
for root, dirs files in os.walk('./'):
    for name in files:
        filename = os.path.join(root, name)
        print (filename)
"""
