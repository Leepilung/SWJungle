# 백준 알고리즘 - 1946 신입 사원
# https://www.acmicpc.net/problem/1946
# 시도 횟수 : 
# 실패 : 
# 통과 : 
import sys
input = sys.stdin.readline
T = int(input().strip()) 

for i in range(0,T):
    N = int(input().strip())
    score = [tuple(map(int,input().split())) for _ in range(N)]
    score.sort(key=lambda x:x[0])

    Cnt = 1
    Min = score[0][1]

    for i in range(1,N):
        if Min > score[i][1]:
            Cnt += 1
            Min = score[i][1]

    print(Cnt)