# 백준 알고리즘 - 11021  A+B - 7
# https://www.acmicpc.net/problem/11021
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
T = int(sys.stdin.readline().strip())

for i in range(1,T+1):
    A, B = map(int, sys.stdin.readline().split())
    print('Case #%d: %d'%(i,A+B))