# 백준 알고리즘 - 10952 A+B - 5
# https://www.acmicpc.net/problem/10952
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0:
        break
    print(A+B)
    