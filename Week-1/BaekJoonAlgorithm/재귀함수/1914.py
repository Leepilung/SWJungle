# 백준 알고리즘 - 1914 하노이 탑
# https://www.acmicpc.net/problem/1914
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
N = int(sys.stdin.readline().strip())
def Hanoi(n :int,start : int,via:int ,end :int):
    if n ==0:
        return

    Hanoi(n-1,start,end,via)    # 시작 -> 끝 -> 과정
    print(start,end)
    Hanoi(n-1,via,start,end)    # 과정 -> 시작 -> 끝

print((2**N)-1) # 결과값은 2의 n승 -1 출력되야함

if N <= 20:
    Hanoi(N,1,2,3)