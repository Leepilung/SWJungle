# 백준 알고리즘 - 18352 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352
# 시도 횟수 : 10
# 실패 : 6
# 통과 : 4

# 개병신문제. visited 초기값을 False나 0으로주면 통과안하고 -1로줘야만 통과함. 도대체 왜??
import sys
from collections import deque
input = sys.stdin.readline
N,M,K,X = map(int,input().split())  

roads = [[] for _ in range(N+1)]
visited = [-1]*(N+1)

for i in range(M):
    a, b = map(int,input().split())
    roads[a].append(b)

def bfs(roads,start,visited):
    queue = deque([start])
    visited[start] = 0

    while queue:
        v = queue.popleft()
        
        for i in roads[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                queue.append(i)

bfs(roads,X,visited)

for i in range(N+1):
    if visited[i] == K:
        print(i)
        
if K not in visited:
    print(-1)