# 백준 알고리즘 - 8393 합
# https://www.acmicpc.net/problem/8393
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
T = int(sys.stdin.readline().strip())
sum = 0
for i in range(1,T+1):
    sum += i
print(sum)