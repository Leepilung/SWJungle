# 백준 알고리즘 - 2675 문자열 반복
# https://www.acmicpc.net/problem/2675
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
T = int(sys.stdin.readline().strip())
count = 0
result = ''

for i in range(T):
    result = ''
    R, S = sys.stdin.readline().split()
    for j in list(S):
        result += j*int(R)
    print(result)