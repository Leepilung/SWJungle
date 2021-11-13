# 백준 알고리즘 - 2110 공유기 설치
# https://www.acmicpc.net/problem/2110
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 

import sys
N,C = map(int,sys.stdin.readline().split())
home = []

for i in range(N):
    home.append(int(sys.stdin.readline().strip()))

home.sort()
def binSearch(arr, start, end):
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        current = arr[0]
        count = 1

        for i in range(1, len(arr)):
            if arr[i] >= current + mid:
                count += 1
                current = arr[i]

        if count >= C:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

    return ans
    

start = 1
end = home[-1]

print(binSearch(home, start, end))