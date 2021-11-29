# 백준 알고리즘 - 2253 점프
# https://www.acmicpc.net/problem/2253
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
a = int((2*N)**0.5 + 1)

jump = [ [float('INF') for _ in range(a)] for _ in range(N)]

print(jump)