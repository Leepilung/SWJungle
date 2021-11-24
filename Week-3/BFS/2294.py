# 백준 알고리즘 - 2294 동전2
# https://www.acmicpc.net/problem/2294
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
input = sys.stdin.readline
N, K = map(int,input().split())
tmp = []
DP = [0 for i in range(K+1)]

for i in range(N):
    tmp.append(int(input()))
for i in range(1, K+1): # 1~15
    a = []
    for j in tmp:   # 1, 5, 12 출력
        if j <= i and DP[i-j] != -1:    # j <= i and DP[i-j] != -1
            a.append(DP[i-j])
    if not a:
        DP[i] = -1
    else:
        DP[i] = min(a) +1
print(DP[K])