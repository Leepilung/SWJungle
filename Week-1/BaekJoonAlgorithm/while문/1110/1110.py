# 백준 알고리즘 - 1110 더하기 사이클
# https://www.acmicpc.net/problem/1110
# 시도 횟수 : 4
# 실패 : 4
# 통과 : 0

import sys
N = int(sys.stdin.readline())
cycle = 0
Ori_N = N
while True:
    if 0 <= N <= 99:
        if N < 10:      # N = 5 
            N = '0' + str(N)     # 05
            A = int(N[-2])+int(N[-1]) # A = 5
            N = int(N[-1] + str(A)[-1])  # N = 55
            cycle += 1
        else:
            N = str(N) # 50
            A = int(N[-2])+int(N[-1]) #  5+0 = 5
            N = int(N[-1] + str(A)[-1])  # 5
            cycle += 1
    if N == Ori_N:
        print(cycle)
        break