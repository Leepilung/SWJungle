# 백준 알고리즘 - 9251 LCS
# https://www.acmicpc.net/problem/9251
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
input = sys.stdin.readline

str1 = list(input().strip())
str2 = list(input().strip())

dp = [ [0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:  # 문자열이 서로 일치할 때
            dp[i][j] = dp[i-1][j-1] + 1
        else: dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])