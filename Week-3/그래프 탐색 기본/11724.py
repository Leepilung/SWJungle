# 백준 알고리즘 - 11724 연결 요소의 개수
# https://www.acmicpc.net/problem/11724
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
adjacent = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

def dfs(v):
    visited[v] = True
    for i in adjacent[v]:
        if not visited[i]:
            dfs(i)
            

for _ in range(M):
    u, v = map(int, input().split())
    adjacent[u].append(v)
    adjacent[v].append(u)
    
for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)