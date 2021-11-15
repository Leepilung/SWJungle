# 백준 알고리즘 - 10828 스택
# https://www.acmicpc.net/problem/10828
# 시도 횟수 : 2
# 실패 : 1
# 통과 : 1

import sys
N = int(sys.stdin.readline().strip())

answer = []

for i in range(N):
    command = sys.stdin.readline().strip()
    if "push" in command:
        number = list(command.split())[-1]
        answer.append(number)
    elif command == "top":
        if len(answer) == 0:
            print(-1)
        else : print(answer[-1])
    elif command == "size":
        print(len(answer))
    elif command == "empty":
        if len(answer) == 0:
            print(1)
        else : print(0)
    elif command == "pop":
        if len(answer) == 0:
            print(-1)
        else: print(answer.pop())