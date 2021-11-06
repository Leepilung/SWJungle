# 백준 알고리즘 - 8958 OX퀴즈
# https://www.acmicpc.net/problem/8958
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
N = int(sys.stdin.readline().strip())

for i in range(N):
    TestCase = list(sys.stdin.readline().strip())
    prev = 0
    acc = 1
    score = 0
    for i in TestCase:
        if i == 'O':
            if prev == 'O':
                acc += 1
                score += acc
                continue
            else:
                prev = 'O'
                acc = 1
                score += acc
                continue
        else:
            acc = 1
            prev ='X'
    print(score)
