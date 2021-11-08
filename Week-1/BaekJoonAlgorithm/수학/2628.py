import sys
from types import coroutine

x, y = map(int, sys.stdin.readline().split())
count = int(sys.stdin.readline().strip())
Xcoordinate = [x]
Ycoordinate = [y]

for i in range(count):
    direction, length = map(int, sys.stdin.readline().split())

    if direction == 0:
        Ycoordinate.append(length)
    else: Xcoordinate.append(length)

xsize = []
ysize = []
xsize.append(Xcoordinate[0])
ysize.append(Ycoordinate[0])
Xcoordinate.sort()
Ycoordinate.sort()

for i in range(0,len(Xcoordinate)-1):
    xsize.append(Xcoordinate[i+1]-Xcoordinate[i])

for i in range(0,len(Ycoordinate)-1):
    ysize.append(Ycoordinate[i+1]-Ycoordinate[i])

max = -10000
for i in xsize:
    for j in ysize:
        if i*j > max:
            max = i*j
print(max)