# 백준 알고리즘 - 10971 외판원 순회2
# https://www.acmicpc.net/problem/10971
# 시도 횟수 : 4
# 실패 : 3
# 통과 : 1

# 1부터 N까지 도시, 도시들 사이에 길있음.
# 한 도시에서 출발해 N개의 도시를 모두 거쳐 원래 도시로 돌아오는 순회 경로 계획
# 한번 간 도시는 다시 갈 수없다.

# 도시간 이동의 비용은 W[i][j] 형태, W[i][j]는 도시 i에서 j로 가는데 비용
# W[i][j]는 W[j][i]와 비용이 다를 수도 있다. 비용은 무조건 양의 정수
# W[i][i]는 항상 0, 경로가 없는 경우에도 W[i][j] = 0
# 주어지는 값은 N과 비용행렬
import sys
from itertools import permutations

N = int(sys.stdin.readline().strip())
cities = list(range(N))
path = [0 for x in range(N)]
for i in range(N):
    path[i] = list(map(int,sys.stdin.readline().split()))

short_path_length = 100000000
for i in permutations(cities,N):
    path_length = 0
    count = 0
    for j in range(N):
        if j != N-1 and path[i[j]][i[j+1]] == 0: break
        if j == N-1:
            if j == N-1 and path[i[j]][i[0]] == 0: break
            path_length += path[i[j]][i[0]]
            count +=1
            continue
        else:
            path_length += path[i[j]][i[j+1]]
            count +=1
    if short_path_length > path_length and count == N:
        short_path_length = path_length

print(short_path_length)



#     if short_path_length > path_length and path_length != 0:
#         short_path_length = path_length

# print(short_path_length)
