# 백준 알고리즘 - 2178  미로 탐색
# https://www.acmicpc.net/problem/2178
# 시도 횟수 : 2
# 실패 : 0
# 통과 : 2

import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
maze = [list(map(int,input().rstrip())) for _ in range(N)]

def bfs(x, y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x,y  = queue.popleft()
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]

            if newX < 0 or newX >= N or newY <0 or newY >= M: continue        

            if maze[newX][newY] == 0: continue

            if maze[newX][newY] == 1:
                maze[newX][newY] = maze[x][y] + 1
                queue.append((newX,newY))
    
    return maze[N-1][M-1]


print(bfs(0,0))