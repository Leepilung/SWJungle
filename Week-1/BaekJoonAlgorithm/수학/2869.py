# 백준 알고리즘 - 2869 달팽이는 올라가고 싶다
# https://www.acmicpc.net/problem/2869
# 시도 횟수 : 2
# 실패 : 1
# 통과 : 1

import sys
import math
A, B, V = map(int, sys.stdin.readline().split())

N = ((V-A)/(A-B))

print(math.ceil(N)+1)