# 백준 알고리즘 - 2439 별 찍기 -2
# https://www.acmicpc.net/problem/2439
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
N = int(sys.stdin.readline().strip())

for i in range(1,N+1):
    print((' '*(N-i))+('*'*i))