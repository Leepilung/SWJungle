# 백준 알고리즘 - 10872 팩토리얼
# https://www.acmicpc.net/problem/10872
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
N = int(sys.stdin.readline().strip())

def factorial(n : int) -> int:
    if n > 0:
        return n * factorial(n-1)

    else:
        return 1

print(factorial(N))