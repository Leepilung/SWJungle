# 백준 알고리즘 - 11725 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
# 시도 횟수 : 5
# 실패 : 4
# 통과 : 1

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
adjacent = [[] for _ in range(N+1)]
visited = [False] * (N+1)
parent = [i for i in range(N+1)]

def dfs(v):
    visited[v] = True
    for i in adjacent[v]:
        if visited[i] == False:
            parent[i] = v
            dfs(i)


for i in range(N-1):
    a, b = map(int, input().split())
    adjacent[a].append(b)
    adjacent[b].append(a)

dfs(1)
for i in parent[2:]:
    print(i)