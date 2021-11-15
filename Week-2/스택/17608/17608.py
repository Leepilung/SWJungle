# 백준 알고리즘 - 17608 막대기
# https://www.acmicpc.net/problem/17608
# 시도 횟수 : 4
# 실패 : 3
# 통과 : 1

import sys
N = int(sys.stdin.readline().strip())
answer = []
for i in range(N):
    answer.append(int(sys.stdin.readline().strip()))

count = 1
max = answer[::-1][0]

for i in answer[::-1]:
    if i > max:
        max = i
        count +=1
print(count)