# 백준 알고리즘 - 2253 점프
# https://www.acmicpc.net/problem/2253
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
input = sys.stdin.readline

N,M = map(int,input().split())

jump = [ [float('INF') *(int((2*N)**0.5 + 2))] for _ in range(N+1)]

jump[1][0] = 0 

stone_set = []
for _ in range(M):
    stone_set.append(int(sys.stdin.readline()))

for i in range(2, N + 1):   # 0행 인덱스는 빈 인덱스, 인덱스값은 각각의 위치
    if i in stone_set:
        continue
    for j in range(1, int((2 * i) ** 0.5) + 1): # 점프는 1부터. i를 이용해 점프 가능한 최댓값을 구하고 그 범위만큼 반복하면서 값 갱신
        jump[i][j] = min(jump[i - j][j - 1], jump[i - j][j], jump[i - j][j + 1]) + 1

if min(jump[N]) == float('inf'):
    print(-1)
else:
    print(min(jump[N]))