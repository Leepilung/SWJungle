# 백준 알고리즘 - 2098 외판원 순회
# https://www.acmicpc.net/problem/2098
# 시도 횟수 : 
# 실패 : 
# 통과 : 

# 이해 복습 무조건적으로 필요. 현재 이해가안감..

import sys

input = sys.stdin.readline

N = int(input().strip())
INF = float('INF')
dp = [[INF]*(1<<N) for _ in range(N)] # 2 ** N 승만큼 배열을 N개만큼 생성

def dfs(x, visited):
    if visited == (1<<N) -1:     # 모든 도시 방문 케이스
        # N이 4일때 dp는 16 즉 15(2진수 표현으로 1111)이면 모든 도시 방문
        if graph[x][0]: # 출발점으로 가는 경로가 없을 때
            return graph[x][0]
        else:   
            return INF

    if dp[x][visited] != INF:   # 이미 최소비용이 계산되어 있는 경우
        return dp[x][visited]

    for i in range(1, N):   # 모든 도시를 탐방
        if not graph[x][i]: # 가는 경로가 없다면 skip
            continue
        if visited & ( 1 << i): # 이미 방문한 도시라면 skip
            continue

    # 점화식 파트
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i))+ graph[x][i])   # | 비트마스크에서 OR 연산자
    return dp[x][visited]

graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))    # 도시 비용 행렬

print(dfs(0,1))