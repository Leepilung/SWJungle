# 백준 알고리즘 - 3055 탈출
# https://www.acmicpc.net/problem/3055
# 시도 횟수 : 
# 실패 : 
# 통과 : 
import sys
from collections import deque
input = sys.stdin.readline
R, C = map(int, input().split())
forest = [list(input().strip()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
queue = deque()

def BFS():
    while queue:
        x, y, w = queue.popleft()
        for dx, dy in ((0,-1),(0,1),(-1,0),(1,0)):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
            if forest[nx][ny] == 'D':
                if w : continue
                return visited[x][y]
            if visited[nx][ny] or forest[nx][ny] == 'X' : continue
            visited[nx][ny] = visited[x][y] +1
            queue.append((nx,ny,w))
    return 'KAKATUS'

for i in range(R):
    for j in range(C):
        if forest[i][j] == '*':
            queue.append((i,j,1))
        if forest[i][j] == 'S':
            start = [i,j]
            visited[i][j] = 1
queue.append((start[0],start[1],0))
print(BFS())