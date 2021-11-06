# 백준 알고리즘 - 1330 두 수 비교하기
# https://www.acmicpc.net/problem/1330
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
A, B = map(int,sys.stdin.readline().split(" "))

if A < B:
    print('<')
if A > B:
    print('>')
if A == B:
    print('==')