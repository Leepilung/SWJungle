# 백준 알고리즘 - 2753 윤년
# https://www.acmicpc.net/problem/2753
# 시도 횟수 : 3
# 실패 : 2
# 통과 : 1

import sys
OddYear = int(sys.stdin.readline().strip())

if OddYear % 4 == 0 and OddYear % 100 != 0 or  OddYear % 400 == 0:
    print(1) 
else:print(0) 