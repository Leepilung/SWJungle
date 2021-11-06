# 백준 알고리즘 - 9488 시험 성적
# https://www.acmicpc.net/problem/9488
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
test = int(sys.stdin.readline().strip())

if test >= 90:
    print('A')
if 90 > test >= 80:
    print('B')
if 80 > test >= 70:
    print('C')
if 70 > test >= 60:
    print('D')
if test < 60:
    print('F')