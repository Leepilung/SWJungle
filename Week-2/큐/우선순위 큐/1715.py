# 백준 알고리즘 - 1715 카드 정렬하기
# https://www.acmicpc.net/problem/1715
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
import heapq
N = int(sys.stdin.readline().strip())
card = []

for _ in range(N):
    heapq.heappush(card, int(sys.stdin.readline()))

if N == 1:
    print(0)
else:
    sum = 0
    while len(card) > 1:
        tmp = heapq.heappop(card) + heapq.heappop(card)
        heapq.heappush(card, tmp)
        sum += tmp
    print(sum)