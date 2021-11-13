# 백준 알고리즘 - 1920 수 찾기 
# https://www.acmicpc.net/problem/1920
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
from typing import List, Sequence

N = int(sys.stdin.readline().strip())
N_list = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
M_list = list(map(int,sys.stdin.readline().split()))

N_list.sort()

def binSearch(a : Sequence, key : int)-> None:

    pl = 0
    pr = len(N_list)-1

    while True:
        pc = (pl+pr) // 2
        if  a[pc] == key:
            return 1
        elif a[pc] < key:
            pl = pc +1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return 0

for i in M_list:
    print(binSearch(N_list,i))