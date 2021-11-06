# 백준 알고리즘 - 2438 별 찍기 -1
# https://www.acmicpc.net/problem/2438
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
N = int(sys.stdin.readline().strip())

for i in range(1,N+1):
    print('*'*i)