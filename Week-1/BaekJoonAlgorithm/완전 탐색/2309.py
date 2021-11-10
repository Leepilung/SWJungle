# 백준 알고리즘 - 2309 일곱 난쟁이
# https://www.acmicpc.net/problem/2309
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
from itertools import combinations

dwarf = [0 for x in range(9)]

for i in range(9):
    dwarf[i] = int(sys.stdin.readline().strip())

for i in combinations(dwarf,7):
    if sum(i) == 100:
        result = list(i)
result.sort()

for i in result:
    print(i)