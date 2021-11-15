# 백준 알고리즘 - 6549 히스토그램에서 가장 큰 직사각형
# https://www.acmicpc.net/problem/6549
# 시도 횟수 : 3
# 실패 : 2
# 통과 : 1

# 현재 높이보다 이전 높이가 높을때만 계산. -> 이전높이가 높아야만 연속적으로 계산가능.
import sys
while True:
    N = list(map(int,sys.stdin.readline().split()))
    n = N[0]
    if n == 0:
        break
    height = [0] + N[1:] + [0]
    check = [0]
    area = 0

    for i in range(1, n + 2):
        while(check and (height[check[-1]] > height[i])):
            cur_height = check.pop()
            area = max(area, (i-check[-1]-1) * height[cur_height])
        check.append(i)
    print(area)