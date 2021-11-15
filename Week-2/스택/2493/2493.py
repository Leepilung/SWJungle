# 백준 알고리즘 - 2493  탑
# https://www.acmicpc.net/problem/2493
# 시도 횟수 : 3
# 실패 : 2
# 통과 : 1

import sys
N = int(sys.stdin.readline().strip())
Towers = list(map(int,sys.stdin.readline().split()))

stack,ans = [],[]
for i in range(N):
    while stack:
        if stack[-1][1] > Towers[i]: 
            ans.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:  
        ans.append(0)

    stack.append([i, Towers[i]]) 

answer = ''
for i in ans:
    answer += str(i) + " "
print(answer[:-1])