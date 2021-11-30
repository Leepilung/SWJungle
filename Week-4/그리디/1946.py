# 백준 알고리즘 - 1946 신입 사원
# https://www.acmicpc.net/problem/1946
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
input = sys.stdin.readline

T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    score = [tuple(map(int,input().split())) for _ in range(N)]
    score.sort(key=lambda x:x[0])
    
    ans = N
    print(score)
