# 백준 알고리즘 - 1707 이분 그래프
# https://www.acmicpc.net/problem/1707
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    visited[x]=1
    q = deque()
    q.append(x) 
    while q: 
        a = q.popleft() 
        for i in queue[a]: 
            if visited[i]==0: 
                visited[i] = -visited[a] 
                q.append(i) 
            else: 
                if visited[i] == visited[a]: 
                    return False 
    return True 
    
k = int(input())    # 테스트 케이스 개수
for i in range(k):
    V, E = map(int, input().split())    # 그래프, 정점 개수
    queue = [[] for i in range(V+1)] 
    visited = [0]*(V+1) 
    flg = 1 
    for j in range(E): 
        a, b = map(int, input().split()) 
        queue[a].append(b) 
        queue[b].append(a) 
    for k in range(1, V+1): 
        if visited[k]==0: 
            if not bfs(k):
                flg = -1 
                break 
    print('YES' if flg==1 else 'NO')
