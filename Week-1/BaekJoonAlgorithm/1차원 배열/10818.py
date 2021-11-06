# 백준 알고리즘 - 10818 최소, 최대
# https://www.acmicpc.net/problem/10818
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
N = int(sys.stdin.readline().strip())
Nums = list(map(int, sys.stdin.readline().rstrip().split(" ")))
result = ""
result += str(min(Nums)) + " "
result += str(max(Nums))
print(result)
