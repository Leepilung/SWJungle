# 백준 알고리즘 - 10773 제로
# https://www.acmicpc.net/problem/10773
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys

K = int(sys.stdin.readline().strip())
ans = []
for i in range(K):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        ans.pop()
    else:
        ans.append(num)

print(sum(ans))