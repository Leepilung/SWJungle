# 백준 알고리즘 - 2164 큐 2
# https://www.acmicpc.net/problem/2164
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
from collections import deque
N = int(sys.stdin.readline().strip())

Nums = deque([x for x in range(1,N+1)])

while len(Nums) != 1:
    Nums.popleft()
    Nums.append(Nums.popleft())

print(Nums[0])