# 백준 알고리즘 - 2908
# https://www.acmicpc.net/problem/2908
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
A, B = sys.stdin.readline().split()
if int(A[::-1]) > int(B[::-1]):
    print(int(A[::-1]))
else: print(int(B[::-1]))