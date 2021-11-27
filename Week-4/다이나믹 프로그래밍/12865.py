# 백준 알고리즘 - 12865 평범한 배낭
# https://www.acmicpc.net/problem/12865
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
items = [(0,0)]
dp = [[ 0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(N):
    a, b = map(int,input().split())
    items.append((a,b))

for i in range(N+1):
    for j in range(K+1):
        w, v = items[i][0], items[i][1]

        if j  < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j])

print(dp[N][K])

# 1차원배열로 푸는 풀이방법 속도,메모리 둘다 덜먹음

N,K = map(int,input().split())
dp = [0]*(K+1)

for _ in range(N):
  W,V = map(int,input().split())
  for i in range(K, W-1, -1):   # 무게순으로 역순
    dp[i] = max(dp[i-W]+V, dp[i])   # dp[i]는 dp[i]와 dp[i-W]+V 

print(dp[K])