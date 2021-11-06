# 백준 알고리즘 - 10430 나머지
# https://www.acmicpc.net/problem/10430
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys

A, B, C = map(int,sys.stdin.readline().split(" "))

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)