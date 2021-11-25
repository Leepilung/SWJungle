# 백준 알고리즘 - 2748 피보나치 수열
# https://www.acmicpc.net/problem/2748
# 시도 횟수 : 2
# 실패 : 0
# 통과 : 2

import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [0] * (n+1)

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    if arr[n] != 0:
        return arr[n]
    
    arr[n] = fibonacci(n-1) + fibonacci(n-2)
    
    return arr[n]

print(fibonacci(n))