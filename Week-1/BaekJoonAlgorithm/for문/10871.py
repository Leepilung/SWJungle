# 백준 알고리즘 - 10871 x보다 작은 수
# https://www.acmicpc.net/problem/10871
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
N, X = map(int, sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().rstrip().split(" ")))
result = ''
for i in A:
    if i < X:
        result += " "+str(i)
#[1,4,2,3]
print(result[1:])
