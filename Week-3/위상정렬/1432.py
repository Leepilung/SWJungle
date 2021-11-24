# 백준 알고리즘 - 1432 그래프 수정
# https://www.acmicpc.net/problem/1432
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
from heapq import heappop, heappush

def topology_sort():
    q = []
    for i in range(1, n + 1):
        if degree[i] == 0:
            # heappush(q, i)
            heappush(q, -i)
    # N = 1
    N = n
    while q:
        now = -heappop(q)
        anw[now] = N

        for k in graph[now]:
            degree[k] -= 1
            if degree[k] == 0:
                heappush(q, -k)
        # N += 1
        N -= 1


n = int(sys.stdin.readline())
anw = [0] * (n + 1)
degree = [0] * (n + 1)  # 진입 차수
graph = [[] for _ in range(n + 1)]  # graph가 도착 정점
for _ in range(1, n + 1):   
    tmp = [0] + list(map(int, sys.stdin.readline().rstrip()))
    for i in range(1, n + 1):
        if tmp[i] == 1:
            # graph[_].append(i)
            # degree[i] += 1
            graph[i].append(_)
            degree[_] += 1
topology_sort()
if anw.count(0) > 1:
    print(-1)
else:
    print(*anw[1:])