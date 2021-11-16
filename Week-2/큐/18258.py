# 백준 알고리즘 - 18258 큐 2
# https://www.acmicpc.net/problem/18258
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
from collections import deque
N = int(sys.stdin.readline().strip())

answer = deque([])
for i in range(N):
    command = sys.stdin.readline().strip()
    if "push" in command:
        answer.append(int(list(command.split())[-1]))
    if command == "front":
        if len(answer) == 0:
            print(-1)
        else: print(answer[0])
    if command == "back":
        if len(answer) == 0:
            print(-1)
        else: print(answer[-1])
    if command == "size":
        print(len(answer))
    if command == "empty":
        if len(answer) == 0:
            print(1)
        else: print(0)
    if command == "pop":
        if len(answer) == 0:
            print(-1)
            continue
        tmp = answer.popleft()
        print(tmp)

