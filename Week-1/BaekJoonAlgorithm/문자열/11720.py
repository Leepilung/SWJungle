# 백준 알고리즘 - 11720 숫자의 합
# https://www.acmicpc.net/problem/11720
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
N = int(sys.stdin.readline().strip())
A = sys.stdin.readline().strip()
sum = 0

for i in list(A):
    sum += int(i)
print(sum)