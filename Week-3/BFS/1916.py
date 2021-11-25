# 백준 알고리즘 - 1916   최소비용 구하기
# https://www.acmicpc.net/problem/1916
# 시도 횟수 : 2
# 실패 : 1
# 통과 : 1

import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)
n= int(input().strip())
m= int(input().strip())
graph = [[] for _ in range(n+1)]
distance = [inf] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start,end = map(int,input().split())

def dijkstra(start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue,(distance[start],start))
    while queue:
        current_distance, now = heapq.heappop(queue)
        if distance[now] < current_distance:
            continue
        for i in graph[now]:
            cost = current_distance + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    return distance

print(dijkstra(start)[end])