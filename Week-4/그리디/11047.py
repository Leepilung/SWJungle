# 백준 알고리즘 - 11047 동전 0 
# https://www.acmicpc.net/problem/11047
# 시도 횟수 : 2
# 실패 : 0
# 통과 : 2

# python3 로는 시간초과.
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

coins = [int(input().strip()) for _ in range(N)]

idx = -1
count = 0
while True:
    if -idx != len(coins) and coins[idx] > K:
        idx += -1
        continue
    if K == 0:
        print(count)    
        break
    K -= coins[idx]
    count += 1


# 속도 개선 풀이
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

coins = [int(input().strip()) for _ in range(N)]
count = 0
for i in coins[::-1]:
    count += K//i
    K -= (K//i) * i

print(count)