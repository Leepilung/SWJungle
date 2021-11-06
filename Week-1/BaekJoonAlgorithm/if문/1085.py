# 백준 알고리즘 - 1085 직사각형에서 탈출
# https://www.acmicpc.net/problem/1085
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
x,y,w,h = map(int, sys.stdin.readline().split())
list = [x,y,w-x,h-y]

print(min(list))
# w-x랑 x랑 비교
# w-x > x인 경우 x와 y-h, y와 비교 가장 작은값

# y-h랑 y랑 비교
