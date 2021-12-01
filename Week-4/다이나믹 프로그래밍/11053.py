# 백준 알고리즘 - 11053 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
input = sys.stdin.readline

N=int(input().strip())
A=list(map(int,input().split()))
dp=[0]*1001
for i in A:
    dp[i]=max(dp[:i])+1

print(max(dp))