from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
flask = [list(map(int,input().split()))for _ in range(N)]
S,X,Y = map(int,input().split())

queue = []
def virus(q):
    while q:
        virus, x, y, time = q.popleft()
        if time == S:
            break
        for dx, dy in ((0,-1),(0,1),(-1,0),(1,0)):
            nx, ny = x + dx, y + dy
            if 0<= nx < N and 0 <= ny < N and flask[nx][ny] == 0:
                flask[nx][ny] = virus
                q.append([virus, nx,ny,time +1])

for i in range(N):
    for j in range(N):
        if flask[i][j] != 0:
            queue.append((flask[i][j], i, j, 0))
queue.sort()
queue = deque(queue)
virus(queue)

print(flask[X-1][Y-1])