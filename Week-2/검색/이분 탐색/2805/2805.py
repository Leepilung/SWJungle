# 백준 알고리즘 - 2805 나무 자르기
# https://www.acmicpc.net/problem/2805
# 시도 횟수 : 6
# 실패 : 5
# 통과 : 1

import sys
N, M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

def binSearch(trees,key, start, end):
    ans = 0
    while start <= end: 
        mid = (start+end) // 2
        sum = 0 
        for i in trees:
            if i >= mid:
                sum += i - mid

        if sum >= key:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    return ans

print(binSearch(trees,M,1,max(trees)))
