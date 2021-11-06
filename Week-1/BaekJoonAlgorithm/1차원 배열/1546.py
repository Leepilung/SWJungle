# 백준 알고리즘 - 1546 평균
# https://www.acmicpc.net/problem/1546
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
N = int(sys.stdin.readline().strip())
Test = list(map(int, sys.stdin.readline().split()))
M = max(Test)
newScore = 0

for i in Test:
    newScore += i/M*100

print(newScore/N)


