# 백준 알고리즘 - 9084 동전
# https://www.acmicpc.net/problem/9084
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
input = sys.stdin.readline

T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    coins = list(map(int,input().split()))
    money = int(input().strip())
    dp = [0 for _ in range(money+1)]    # 돈의 최대치까지 배열 생성
    dp[0] = 1
    for i in coins: # 코인 하나씩 꺼내옴
        for j in range(1,money+1):
            if j - i >= 0:  # 꺼내온 코인의 사용가능 유무 판단 로직
                dp[j] += dp[j - i]
    print(dp[money])

