# 백준 알고리즘 - 1939  중량제한
# https://www.acmicpc.net/problem/1939
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
bridge = [[] for _ in range(N + 1)]

for i in range(M):
    a, b, w = map(int, input().split())
    bridge[a].append([b, w])
    bridge[b].append([a, w])

s, e = map(int, input().split())
low, high = 1, 10e9

def bfs(mid):
    visit[s] = 1
    q = deque()
    q.append(s)
    while q:
        start = q.popleft()
        if start == e: 
            return True
        for goal, weight in bridge[start]:
            if visit[goal] == 0 and mid <= weight:
                q.append(goal)
                visit[goal] = 1
    return False

while low <= high:
    visit = [0 for i in range(N + 1)]
    mid = (low + high) // 2
    if bfs(mid): low = mid + 1
    else: high = mid - 1

print(int(high))