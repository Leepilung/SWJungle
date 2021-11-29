# 백준 알고리즘 - 1904 01타일
# https://www.acmicpc.net/problem/1904
# 시도 횟수 : 20
# 실패 : 17
# 통과 : 3

import sys
input = sys.stdin.readline
N = int(input().strip())

a = 0
b = 1

for i in range(N):
    a,b = b,(a+b)%15746

print(b)