# 백준 알고리즘 - 9663 N - Queen
# https://www.acmicpc.net/problem/9663
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
N = int(sys.stdin.readline().strip())
pos = [0] * N   # 각 열에서 퀸의 위치
xFlag = [False] * N    #각 행에 퀸을 배치했는지 체크하는 깃발
rightDigonal_Flag = [False] * (N*2-1) # 우상하향 깃발
leftDigonal_Flag = [False] * (N*2-1)   # 좌상하향 깃발

global count
count = 0

def set(i:int) -> None:
    global count
    for j in range(N):  # 열에 배치하는 로직
        if (    not xFlag[j]    # 행체크 로직
            and not rightDigonal_Flag[i+j]  # 우상하향 대각선 체크 로직
            and not leftDigonal_Flag[i-j+(N-1)]): # 좌상하향 대각선 체크 로직
            pos[i] = j
            if i == N-1:
                count +=1
            else:
                xFlag[j] = rightDigonal_Flag[i+j] = leftDigonal_Flag[i-j+(N-1)] = True   
                set(i+1)
                xFlag[j] = rightDigonal_Flag[i+j] = leftDigonal_Flag[i-j+(N-1)] = False

set(0)
print(count)

