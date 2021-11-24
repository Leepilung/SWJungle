# 백준 알고리즘 -  2637 장난감 조립
# https://www.acmicpc.net/problem/2637
# 시도 횟수 : 3
# 실패 : 2
# 통과 : 1

import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
parts = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
outdegree = [0] * (N+1)
acc = [0] * (N+1)

for i in range(1,M+1):
    a,b,c = map(int,input().split())
    parts[a].append((b,c))
    outdegree[a] += 1
    indegree[b] += 1

def topologySort ():
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        now = queue.popleft()
        for i, weight in parts[now]:
            if acc[now] != 0:
                weight *= acc[now]
            indegree[i] -= 1
            acc[i] += 1*weight
            if indegree[i] == 0:
                queue.append(i)
topologySort()
for i in range(1,N+1):
    if outdegree[i] ==0:
        print(i,end=" ")
        print(acc[i])