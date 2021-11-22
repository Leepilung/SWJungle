# 백준 알고리즘 - 2617 구슬찾기
# https://www.acmicpc.net/problem/2617
# 시도 횟수 : 4
# 실패 : 2
# 통과 : 2

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
bead = [list(map(int,input().split())) for _ in range(M)] 

heavy = [[] for _ in range(N+1)]
light = [[] for _ in range(N+1)]

for a,b in bead:
    heavy[b].append(a)
    light[a].append(b)

def dfs(v,arr):
    cnt = 0
    visited[v] = True

    for i in arr[v]:
        if visited[i] == True:
            continue
        cnt += 1
        cnt += dfs(i,arr)
    return cnt    


ans = 0
mid = (N+1)/2
for i in range(1,N+1):
    visited = [False]*(N+1)
    if mid <=dfs(i,heavy) or mid <= dfs(i,light):
        ans +=1

print(ans)