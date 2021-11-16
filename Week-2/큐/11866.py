# 백준 알고리즘 - 11866 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())
circle = deque([x for x in range(1,N+1)])

answer = []
while len(answer) != N:
    count = 1
    for _ in range(K):
        if count == K:
            answer.append(circle.popleft())
            break
        count +=1
        circle.append(circle.popleft())

ans = '<'
for i in answer:
    ans += str(i)+', '
ans = ans[:-2] +'>'
print(ans)