# 백준 알고리즘 - 7569 토마토
# https://www.acmicpc.net/problem/
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())

tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):

            if tomatoes[i][j][k] == 1:
                queue.append((i, j, k))

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if tomatoes[nz][nx][ny] == 0:
                    tomatoes[nz][nx][ny] = tomatoes[z][x][y] + 1
                    queue.append((nz, nx, ny))

bfs()

flag = False
answer = -1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatoes[i][j][k] == 0:
                flag = True
                
            answer = max(answer, tomatoes[i][j][k])
if flag:
    answer = -1
elif answer == 1:
    answer = 0
else:
    answer -= 1

print(answer)