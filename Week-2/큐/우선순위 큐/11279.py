# 백준 알고리즘 - 11279 최대 힙
# https://www.acmicpc.net/problem/11279
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import heapq
import sys
n = int(sys.stdin.readline())
answer = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        try:
            print(-heapq.heappop(answer))
        except:
            print(0)
    else:
        heapq.heappush(answer,-num)