# 백준 알고리즘 - 14888 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
input = sys.stdin.readline

N = int(input())
Nums = list(map(int,input().split()))
operator = list(map(int,input().split()))


def dfs(depth, sum, plus,minus,multi,divide):
    global maxNum, minNum
    if depth == N:
        maxNum = max(sum,maxNum)
        minNum = min(sum,minNum)
        return

    if plus:
        dfs(depth + 1, sum + Nums[depth], plus - 1, minus, multi, divide)
    if minus:
        dfs(depth + 1, sum - Nums[depth], plus, minus - 1, multi, divide)
    if multi:
        dfs(depth + 1, sum * Nums[depth], plus, minus, multi - 1, divide)
    if divide:
        dfs(depth + 1, int(sum / Nums[depth]), plus, minus, multi, divide - 1)

maxNum = -100000000000
minNum = 100000000000

dfs(1,Nums[0],operator[0],operator[1],operator[2],operator[3])
print(maxNum)
print(minNum)