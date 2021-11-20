# 백준 알고리즘 - 1197 최소 스패닝 트리
# https://www.acmicpc.net/problem/1197
# 시도 횟수 : 0
# 실패 : 0
# 통과 : 0

from sys import stdin
input = stdin.readline

V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]
graph.sort(key=lambda x: x[2])

ans = 0
parent = [i for i in range(V+1)]

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])  # 경로 압축
    return parent[a]

def union(a, b):
    a,b = find(a),find(b)
    parent[b] = a

for i in graph:
    a, b, c = i

    if find(a) != find(b): # 싸이클인지 아닌지 확인하는 구문
        union(a,b)
        ans +=c
print(ans)