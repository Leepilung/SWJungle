# 백준 알고리즘 - 1931 회의실 배정
# https://www.acmicpc.net/problem/1931
# 시도 횟수 : 3
# 실패 : 1
# 통과 : 2

import sys
input = sys.stdin.readline

N = int(input().strip())
county = []
for i in range(N):
    county.append(tuple(map(int,input().split())))

county.sort(key=lambda x : (x[1],x[0]))

ans = 1 
s, e = county[0][0],county[0][1]
for i in range(1,len(county)):
    start,end = county[i][0], county[i][1]
    if start < e:
        continue
    elif start >= e:
        ans += 1
        e = end
        continue
print(ans)