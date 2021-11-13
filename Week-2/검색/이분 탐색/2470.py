# 백준 알고리즘 - 2470 두 용액
# https://www.acmicpc.net/problem/2470
# 시도 횟수 : 2
# 실패 : 1
# 통과 : 1

import sys
N = int(sys.stdin.readline().strip())
liquids = [int(x) for x in sys.stdin.readline().split()]
liquids.sort()  

def binSearch(liquids,start,end):
    ans = (liquids[start]+liquids[end])
    ans_start = start
    ans_end = end
    while start < end:
        mid = liquids[start]+liquids[end]
        
        if abs(mid) < abs(ans):
            ans = mid
            ans_start = start
            ans_end = end
            if ans == 0:
                return print(liquids[ans_start],liquids[ans_end])
        if mid < 0:
            start += 1
        else: 
            end -=1
    return print(liquids[ans_start],liquids[ans_end])
start = 0
end = N-1
binSearch(liquids,start,end)

