# 백준 알고리즘 - 2606 바이러스
# https://www.acmicpc.net/problem/2606
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
input = sys.stdin.readline

N = int(input())
pair = int(input())
adjcant = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0

def dfs(v):
    global count
    visited[v] = True
    for i in adjcant[v]:
        if not visited[i]:
            count +=1
            dfs(i)

for _ in range(pair):
    a, b = map(int, input().split())
    adjcant[a].append(b)
    adjcant[b].append(a)

dfs(1)
print(count)