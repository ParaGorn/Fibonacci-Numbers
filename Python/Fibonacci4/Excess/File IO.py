import os, glob


def solution():
    x = 0
    for fn in glob.glob("*.fib"):
        y = int(fn[:-4])
        if y > x:
            x = y
        #print (fn[:-4])
    print (x)

solution()

"""
os.startfile(fn)
for root, dirs files in os.walk('./'):
    for name in files:
        filename = os.path.join(root, name)
        print (filename)
"""
