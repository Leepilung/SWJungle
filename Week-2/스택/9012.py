# 백준 알고리즘 - 9012
# https://www.acmicpc.net/problem/9012
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
T = int(sys.stdin.readline().strip())

for i in range(T):
    answer = []
    case = sys.stdin.readline().strip()
    for j in case:
        if j == "(":
            answer.append(j)
        elif j == ")" and len(answer) != 0:
            if answer[-1] == "(":
                answer.pop()
        else:
            answer.append(j)
    if len(answer) == 0:
        print('YES')
    else: print('NO')