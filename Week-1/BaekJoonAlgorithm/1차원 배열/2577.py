# 백준 알고리즘 - 2577 숫자의 개수
# https://www.acmicpc.net/problem/2577
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())

result = list(str(A*B*C))
count = [0 for i in range(10)]

for i in result:
    for j in range(10):
        if int(i) == j:
            count[j] +=1

for i in count:
    print(i)