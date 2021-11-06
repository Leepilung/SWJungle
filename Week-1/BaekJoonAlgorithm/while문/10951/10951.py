# 백준 알고리즘 - 10951 A+B -4
# https://www.acmicpc.net/problem/10951
# 시도 횟수 : 0
# 실패 : 0
# 통과 : 0

import sys
while True:
    try:
        A, B = map(int,sys.stdin.readline().split(" "))
    except:
        break
    if 0 < A and B < 10:
        print(A+B)