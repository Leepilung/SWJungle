# 백준 알고리즘 - 10869 사칙연산
# https://www.acmicpc.net/problem/10869
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys

A, B = map(int,sys.stdin.readline().split(" "))

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)