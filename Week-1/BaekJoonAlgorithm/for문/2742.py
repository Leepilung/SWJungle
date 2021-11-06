# 백준 알고리즘 - 2742  기찍 N 
# https://www.acmicpc.net/problem/2742
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
N = int(sys.stdin.readline().strip())
for i in range(N):
    print(N-i)