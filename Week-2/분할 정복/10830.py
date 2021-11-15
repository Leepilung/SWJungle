# 백준 알고리즘 - 10830 행렬 제곱
# https://www.acmicpc.net/problem/10830
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys

N, B = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def sqrtArray(N,arr,arr2):
    answer = [[0 for _ in range(N)] for _ in range(N)]  # N x N 행렬

    for i in range(N):
        for j in range(N):
            for k in range(N):
                answer[i][j] += arr[i][k] * arr2[k][j]
            answer[i][j] %= 1000

    return answer

def divide(N,B,arr):
    if B == 1:
        return arr
    elif B == 2:
        return sqrtArray(N,arr,arr)
    else:
        ans = divide(N,B//2,arr)
        if B % 2 == 0:
            return sqrtArray(N,ans,ans)
        else:
            return sqrtArray(N,sqrtArray(N,ans,ans),arr)

ans = divide(N,B,A)
for i in ans:
    for j in i:
        print(j%1000, end=" ")
    print()