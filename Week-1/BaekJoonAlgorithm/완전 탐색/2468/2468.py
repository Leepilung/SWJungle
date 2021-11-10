# 백준 알고리즘 - 2468 안전지대
# https://www.acmicpc.net/problem/2468
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys, copy
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline().strip())
main_area = [0 for _ in range(N)]
for i in range(N):
    main_area[i] = list(map(int,sys.stdin.readline().split()))

high = - 100000
for i in main_area:
    if high < max(i):
        high = max(i)

class Solution:
    def numsafeArea (self,depth:int,area):
        count = 0
        for y in range(len(area)):
            for x in range(len(area[0])):
                if area[y][x] > depth:
                    self.count(depth,area,y,x)
                    count += 1
        return count
                    
    def count (self,depth:int,area,y,x):
        if y < 0 or x < 0 or y>=len(area) or x>=len(area[0]) or area[y][x] <= depth:
            return
        area[y][x] = 0
        self.count(depth,area, y+1, x)
        self.count(depth,area, y-1, x)
        self.count(depth,area, y, x+1)
        self.count(depth,area, y, x-1)

cal = Solution()
answer = 0
for i in range(1,high+1):
    area = copy.deepcopy(main_area)
    num = cal.numsafeArea(i,area)
    max(answer,num)
    
print(answer)
    
