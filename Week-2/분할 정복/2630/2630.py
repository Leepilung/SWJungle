# 백준 알고리즘 - 2630 색종이 만들기
# https://www.acmicpc.net/problem/2630
# 시도 횟수 : 2
# 실패 : 1
# 통과 : 1

import sys

N = int(sys.stdin.readline().strip())
paper = []
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

white, blue = 0,0

# N이 8일때 1사분면 -> 0~3, 0~3 // 2사분면 -> 0~3,4~7 // 3사분면 4~7, 0~3 // 4사분면 4~7,4~7
def DivideAndCount(y,x,N):
    global white, blue
    color = paper[y][x]
    for i in range(y,y+N):
        for j in range(x,x+N):
            if color != paper[i][j]:
                DivideAndCount(y,x,N//2)
                DivideAndCount(y,x+N//2,N//2)
                DivideAndCount(y+N//2,x,N//2)
                DivideAndCount(y+N//2,x+N//2,N//2)
                return
    if color == 0:
        white += 1
    else: blue += 1

DivideAndCount(0,0,N)
print(white)
print(blue)