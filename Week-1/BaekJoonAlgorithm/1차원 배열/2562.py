# 백준 알고리즘 - 2562 최댓값
# https://www.acmicpc.net/problem/2562
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys

max = 0
max_index = 0

for i in range(9):
    T = int(sys.stdin.readline().strip())
    if T > max:
        max = T
        max_index = i+1

print(max)
print(max_index)