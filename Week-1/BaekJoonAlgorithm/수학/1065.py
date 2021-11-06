# 백준 알고리즘 - 한수
# https://www.acmicpc.net/problem/1065
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
N = int(sys.stdin.readline())

def Hansoo (N):
    if N >= 100:
        num = 99
        for i in range(100,N+1):
            N = str(i)
            a = int(N[0])-int(N[1])
            b = int(N[1])-int(N[2])
            if a == b:
                num +=1
    else: # N < 100
        num = N
    print(num)
