# 백준 알고리즘 - 15552 빠른 A+B
# https://www.acmicpc.net/problem/15552
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
T = int(sys.stdin.readline().strip())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split(" "))
    print(A+B)
