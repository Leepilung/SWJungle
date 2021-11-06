# 백준 알고리즘 - 2739 구구단
# https://www.acmicpc.net/problem/2739
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
N = int(sys.stdin.readline())

for i in range(1,10):
    print('%d * %d = %d'%(N,i,N*i))