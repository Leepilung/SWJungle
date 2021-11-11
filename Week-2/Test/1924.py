# 백준 알고리즘 - 1924 2007년
# https://www.acmicpc.net/problem/1924
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
month, day = map(int,sys.stdin.readline().split())

days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day_of_week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
total = 0
for i in range(1,month):
    total += days[i]
total += day
print(day_of_week[total%7])
