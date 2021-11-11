# 백준 알고리즘 - 6603 로또
# https://www.acmicpc.net/problem/6603
# 시도 횟수 : 3
# 실패 : 2
# 통과 : 1

import sys
from itertools import combinations

while True:
    Test= list(map(int,sys.stdin.readline().split()))
    S = Test[1:]
    K = Test[0]
    if K == 0:
        break
    for i in combinations(S,6):
        print(*i)
    print("")