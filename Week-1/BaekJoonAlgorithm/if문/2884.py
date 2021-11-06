# 백준 알고리즘 - 2884 알람 시계
# https://www.acmicpc.net/problem/2884
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

# 알람을 45분 앞선시간으로 바꾼다.
# M이 45보다 크면 -45 아니면 H를 -1 M에 + 15

import sys
H, M = map(int,sys.stdin.readline().split(" "))

if M >= 45:
    print(H,M-45)
else:
    if H == 0:
        H = 24
        print(H-1,M+15)
    else:
        print(H-1,M+15)