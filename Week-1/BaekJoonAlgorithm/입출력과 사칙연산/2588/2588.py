# 백준 알고리즘 - 2588 곱셈
# https://www.acmicpc.net/problem/2588
# 시도 횟수 : 2
# 실패 : 1
# 통과 : 1
import sys

A = int(sys.stdin.readline().strip())
B = sys.stdin.readline().strip()

for i in list(B)[::-1]:
    print(A*int(i))
print(A*int(B))