# 백준 알고리즘 - 1074 Z
# https://www.acmicpc.net/problem/1074
# 시도 횟수 : 
# 실패 : 
# 통과 : 
import sys

N,r,c = map(int, sys.stdin.readline().split())

turn = 0

N1 = [[0,1],[2,3]]

def Z(N:int,r:int,c:int)->None:
    print(N,'번째 시작')
    dot = 2**(N-1)
    global turn

        
    if N == 1:
        r, c = r % 2, c % 2
        turn += N1[r][c]
        print('가산 값 : ',r,c,N1[r][c])
        return
    else:
        if c < dot and r < dot:
            quadrant = 1
        if c >= dot and r < dot:
            quadrant = 2
        if c < dot and r >= dot:
            quadrant = 3
        if c >= dot and r >= dot:
            quadrant = 4
        print('입력값 :',N,"r :",r,"c :",c,'Dot :',dot,'사분면 : ',quadrant)  
        add_size = (4**(N-1))*(quadrant-1)
        dot = dot // 2
 
        if r == 1:
            r = r % 2
        else : r = r // 2
        if c == 1:
            c = c % 2
        else : c = c // 2
        print('바뀐 c,r', c,r,dot)
        turn += add_size
        print('에드 사이즈 : ',add_size)
        Z(N-1,r,c)

Z(N,r,c)
print(turn)