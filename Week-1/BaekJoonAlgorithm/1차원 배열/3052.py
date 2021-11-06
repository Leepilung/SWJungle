# 백준 알고리즘 - 3052 나머지
# https://www.acmicpc.net/problem/3052
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys

Nums = []

for i in range(10):
    T = int(sys.stdin.readline().strip())
    if (T % 42) not in Nums:
        Nums.append(T%42)
print(len(Nums))