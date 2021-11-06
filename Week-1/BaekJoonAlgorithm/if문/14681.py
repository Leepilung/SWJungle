# 백준 알고리즘 - 14681 사분면 고르기
# https://www.acmicpc.net/problem/14681
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
x = int(sys.stdin.readline().strip())
y = int(sys.stdin.readline().strip())

if x > 0 and y > 0:
    print(1)
if x < 0 and y > 0:
    print(2)
if x < 0 and y < 0:
    print(3)
if x > 0 and y < 0:
    print(4)