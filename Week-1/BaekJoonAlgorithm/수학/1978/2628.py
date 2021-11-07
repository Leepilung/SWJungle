# 백준 알고리즘 - 2628 종이자르기
# https://www.acmicpc.net/problem/2628
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

# 입력 1 -> 종이의 크기 (가로 세로 길이)
# 입력 2 -> 종이를 자를 횟수
# 입력 3 ~ 5 -> 종이 자르는 지점
# 이 때 가장 큰 종이의 넓이 출력
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
Xcoordinate.sort()
xsize.append(Xcoordinate[0])
Ycoordinate.sort()
ysize.append(Ycoordinate[0])

if len(Xcoordinate) > 1 and len(Xcoordinate) == 2:
    xsize.append(Xcoordinate[1]-Xcoordinate[0])
elif len(Xcoordinate) >=3:
    for i in range(0,len(Xcoordinate)-1):
        xsize.append(Xcoordinate[i+1]-Xcoordinate[i])

if len(Ycoordinate) > 1 and len(Ycoordinate) == 2:
    ysize.append(Ycoordinate[1]-Ycoordinate[0])
elif len(Ycoordinate) >=3:
    for i in range(0,len(Ycoordinate)-1):
        ysize.append(Ycoordinate[i+1]-Ycoordinate[i])

max = -10000
for i in xsize:
    for j in ysize:
        if i*j > max:
            max = i*j
print(max)