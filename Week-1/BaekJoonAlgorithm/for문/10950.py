# 백준 알고리즘 - 
# https://www.acmicpc.net/problem/
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
T = int(sys.stdin.readline().strip())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)