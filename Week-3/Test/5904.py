# 백준 알고리즘 - 5904 Moo 게임
# https://www.acmicpc.net/problem/5904
# 시도 횟수 : 
# 실패 : 
# 통과 : 
import sys 
N = int(sys.stdin.readline())

while N > 3:
    k = 3
    inc = 4
    while k < N:
        k *= 2
        k += inc
        inc += 1     # While 문 반복 시 inc 1 증가.
    inc -= 1
    k = (k - inc) / 2
    N -= k
    if N < inc:
        if N == 1:
            print('m')
            exit(0)
        else:
            print('o')
            exit(0)
    else:
        N -= inc
# N이 3이하일 때
if N == 1:
    print('m')
else:
    print('o')
