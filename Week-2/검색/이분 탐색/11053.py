# 백준 알고리즘 - 11053 가장 긴 증가하는 부분
# https://www.acmicpc.net/problem/11053
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
N = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().split()))


def binSearch_left(arr,key):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start+end)//2
        if arr[mid] < key: start = mid + 1
        else: end = mid
    return start

Check = [A[0]]

for i in range(1,N):
    if A[i] > Check[-1]:
        Check.append(A[i])
    else:
        idx = binSearch_left(Check,A[i])    #A[i]가  Check에 삽입될 수 있는 인덱스의 좌측 인덱스가 반환됨.
        Check[idx] = A[i]

print(len(Check))
