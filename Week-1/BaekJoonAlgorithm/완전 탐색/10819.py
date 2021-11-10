# 백준 알고리즘 - 10819 차이를 최대로
# https://www.acmicpc.net/problem/10819
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
from itertools import permutations
N = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().split()))
result = []
max = -10000
for i in permutations(A,N):
    result = []
    for j in range(N-1):
        result.append(abs(i[j+1]-i[j]))
        resultSum = sum(result)
    if max < resultSum:
        max = resultSum
print(max)