# 백준 알고리즘 - 1541 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
input = sys.stdin.readline
formula = input().split('-')
ans = 0

for i in range(len(formula)):
    if '+' in formula[i]:
        b = list(map(int,formula[i].split('+')))
        formula[i] = sum(b)
        continue

sum = int(formula[0])

for j in formula[1:]:
    if str(type(j)) == "<class 'str'>":
        sum -= int(j)
    else:
        sum -= j