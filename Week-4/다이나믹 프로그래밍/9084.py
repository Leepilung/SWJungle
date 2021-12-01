# 백준 알고리즘 - 9084 동전
# https://www.acmicpc.net/problem/9084
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
input = sys.stdin.readline

T = int(input().strip())    # 테스트 케이스의 개수

for i in range(T):  
    N = int(input().strip())    # 동전의 가지 수
    coins = list(map(int,input().split()))  # 동전 종류
    money = int(input().strip())    # 금액
    dp = [0 for _ in range(money+1)]    # 돈의 최대치까지 배열 생성
    dp[0] = 1
    for i in coins: # 코인 하나씩 꺼내옴
        for j in range(1,money+1):  # 1부터 money+1까지 dp 순회
            if j - i >= 0:  #
                dp[j] += dp[j - i]
    print(dp[money])

