# 백준 알고리즘 - 2252 줄 세우기
# https://www.acmicpc.net/problem/2252
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for i in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    A,B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

def topologySort ():
    ans = []
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        now = queue.popleft()
        ans.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    for i in ans:
        print(i, end=' ')

topologySort()