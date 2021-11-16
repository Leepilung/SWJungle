# 백준 알고리즘 - 3190 뱀
# https://www.acmicpc.net/problem/3190
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
from collections import deque

N = int(sys.stdin.readline()) 
K = int(sys.stdin.readline()) 

board = [[1]*(N+2)] + [[1]+[0]*N+[1] for _ in range(N)] + [[1]*(N+2)]

for i in range(K):
    r,c = map(int, sys.stdin.readline().split()) 
    board[r][c] = 'A'
    
L = int(sys.stdin.readline()) 
instruction = list(map(lambda x:[int(x[0]), x[1]], [sys.stdin.readline().split() for _ in range(L)]))

time = 0 
x,y = 1,1
direction = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)} # 0:북 1:동 2:남 3:서
# 북일때는 x값 감소, 남일때는 x값 증가, 동일때는 y값 증가, 서일때는 y값 감소
d = 1
snake_position = deque([[1,1]])

board[1][1] = 3

while(1):
    x = x + direction[d][0]
    y = y + direction[d][1]
    
    if board[x][y] == 'A':
        board[x][y] = 3 
        snake_position.append([x, y]) 
        time = time + 1

    elif board[x][y] == 0:
        board[x][y] = 3
        snake_position.append([x,y])
        del_x, del_y = snake_position.popleft() 
        board[del_x][del_y] = 0
        time = time + 1

    else:
        time = time + 1
        break

    if len(instruction) != 0:
        if instruction[0][0] == time:
            if instruction[0][1] == 'L': # 왼쪽으로 90도 회전
                d = (d-1)%4
            elif instruction[0][1] =='D': # 오른쪽으로 90도 회전
                d = (d+1)%4
            del instruction[0] # 방향전환 완료 -> 삭제

print(time)