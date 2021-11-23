# 백준 알고리즘 - 2665  미로 만들기
# https://www.acmicpc.net/problem/2665
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
import heapq

input = sys.stdin.readline
N = int(input().strip())
room = [list(map(int,input().strip())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

def dijkstra():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    heap = []
    heapq.heappush(heap,[0,0,0])
    visited[0][0] = 1
    while heap:
        a, x, y = heapq.heappop(heap)
        if x == N-1 and y == N-1:
            print(a)
            return
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]

            if 0 <= newX < N and 0 <= newY < N and visited[newX][newY] == 0:
                visited[newX][newY] = 1
                if room[newX][newY] == 0:
                    heapq.heappush(heap, [a+1,newX,newY])
                else: heapq.heappush(heap, [a,newX,newY])

dijkstra()