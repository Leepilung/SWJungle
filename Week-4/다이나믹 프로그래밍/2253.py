# 백준 알고리즘 - 2253 점프
# https://www.acmicpc.net/problem/2253
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
input = sys.stdin.readline
N,M = map(int,input().split())
a = int((2*N)**0.5 + 1)

jump = [ [float('INF') for _ in range(a+1)] for _ in range(N+1)]
jump[1][0] = 0 

stone_set = set(int(sys.stdin.readline()) for _ in range(M))

for i in range(2, N + 1):
    if i in stone_set:
        continue
    for j in range(1, a): 
        jump[i][j] = min(jump[i - j][j - 1], jump[i - j][j], jump[i - j][j + 1]) + 1

if min(jump[N]) == float('inf'):
    print(-1)
else:
    print(min(jump[N]))