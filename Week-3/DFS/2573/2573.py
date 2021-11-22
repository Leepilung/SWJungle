# 백준 알고리즘 - 2573 빙산
# https://www.acmicpc.net/problem/2573
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys,copy
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N,M = map(int,input().split())
iceberg = [list(map(int,input().split())) for _ in range(N)]
year = 0

def Check(y,x):
    if check[y][x] == 0 or check[y][x] == '*':
        return
    if 0 <= y < N:
        if 0 <= x < M:
            check[y][x] = '*'
            Check(y,x-1)
            Check(y,x+1)
            Check(y-1,x)
            Check(y+1,x)

def afterYear(y,x,check,sea):
    if check[y][x] != 0:
        if 0 <= y -1 < N and check[y-1][x] ==0 :
            sea += 1
        if 0 <= y +1 < N and check[y+1][x] ==0:
            sea += 1
        if 0 <= x -1 < M and check[y][x-1] ==0:
            sea += 1
        if 0 <= x +1 < M and check[y][x+1] ==0:
            sea += 1
    return sea

while True:
    count = 0
    check = copy.deepcopy(iceberg)
    for i in range(N):
        for j in range(M):
            if check[i][j] != 0 and check[i][j] != '*':
                Check(i,j)
                count += 1
    if count >= 2:
        print(year)
        break
    if count == 0:
        print(0)
        break
    for i in range(N):
        for j in range(M):
            if check[i][j] != 0:
                sea = afterYear(i,j,check,0)
                iceberg[i][j] -= sea
                if iceberg[i][j] <= 0:
                    iceberg[i][j] = 0
    year += 1