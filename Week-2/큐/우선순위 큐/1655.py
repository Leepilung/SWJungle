# 백준 알고리즘 - 1655 가운데를 말해요
# https://www.acmicpc.net/problem/1655
# 시도 횟수 : 0
# 실패 : 0
# 통과 : 0

import sys
import heapq
N = int(sys.stdin.readline().strip())

min_h, max_h = [], []
answer = []
for i in range(N):
    num = int(sys.stdin.readline().strip())
    
    if len(min_h) == len(max_h):
        heapq.heappush(max_h, (-num, num))
    else:
        heapq.heappush(min_h, (num,num))
    if min_h and max_h[0][1] > min_h[0][0]:
        min=heapq.heappop(min_h)[0]
        max=heapq.heappop(max_h)[1]
        heapq.heappush(max_h, (-min, min))
        heapq.heappush(min_h, (max, max))
    
    answer.append(max_h[0][1])

for i in answer:
    print(i)