# 백준 알고리즘 - 1629 곱셈
# https://www.acmicpc.net/problem/1629
# 시도 횟수 : 2
# 실패 : 1
# 통과 : 1
# A를 B번 곱한 수를 C로 나눈 나머지를 구하라

import sys
A, B, C = map(int,sys.stdin.readline().split())

def divmod(A,B,C):
    if B == 1:
        return A % C
    else:
        ans = divmod(A,B//2,C)
        if B % 2 == 0:
            return ans**2 % C
        else: return ans**2 * A % C     # (A%C) * (A%C) * (A%C)

print(divmod(A,B,C))