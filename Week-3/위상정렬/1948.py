# 백준 알고리즘 - 1948 임계경로
# https://www.acmicpc.net/problem/1948
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
in_degree = [0] * (n+1)
out_degree = [0] * (n+1)
arr = [[] for _ in range(n+1)]
revers_arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    in_degree[b]+=1
    out_degree[a]+=1
    arr[a].append([b,c])
    revers_arr[b].append([a,c])

start, end = map(int, sys.stdin.readline().split())

q = deque()
q.append(start)

cost = [0] * (n+1)
cost[start] = 0

while q:
    now = q.popleft()
    for i in arr[now]:
        in_degree[i[0]] -= 1
        if in_degree[i[0]] == 0 :
            q.append(i[0])
        if cost[i[0]] < (cost[now] + i[1]):
            cost[i[0]] = cost[now] + i[1]


print(cost[end])

q.append(end)
visited = [False] * (n+1)

cnt = 0
while q:
    now = q.popleft()
    visited[now]=True
    for i in revers_arr[now]:
        out_degree[i[0]] -= 1
        if cost[i[0]] == cost[now] - i[1]:
            cnt+=1
            if visited[i[0]] == False:
                visited[i[0]] = True
                q.append(i[0])
print(cnt)