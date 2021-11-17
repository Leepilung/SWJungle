# 백준 알고리즘 - 13334 철로
# https://www.acmicpc.net/problem/13334
# 시도 횟수 : 0
# 실패 : 0
# 통과 : 0

import sys
import heapq

n = int(sys.stdin.readline())
road_info = []
for _ in range(n):
    road = list(map(int, sys.stdin.readline().split()))
    road_info.append(road)

d = int(sys.stdin.readline())
roads = []
for road in road_info:
    house, office = road
    if abs(house - office) <= d:    # 거리가 아예 안되는 경우들은 제외
        road = sorted(road)
        roads.append(road)  # 부합되는 값들 별도의 배열(roads)에 저장
roads.sort(key=lambda x:x[1])   # 더 멀리있는 좌표값에서 왼쪽으로 철로를 깔기 떄문에 x[1]값을 기준

answer = 0
heap = []
for road in roads:  # roads에 있는 값들을 하나씩 꺼내온다,
    if not heap:
        heapq.heappush(heap, road)  # 비어 있으면 일단 넣음
    else:
        while heap[0][0] < road[1] - d: #  heap[0][0]가 기준점. 
                            # 조건 충족은 기준점보다 더 먼 거리임을 의미
            heapq.heappop(heap) # 기준점을 초기화. 입력값(road)와 비교.
            if not heap:
                break
        heapq.heappush(heap, road)  # while문 조건 부합 시 기준점들을 초기화시키고 아닐 경우 그냥 넣음
    answer = max(answer, len(heap)) # 각 지점마다 가능한 갯수를 갱신하면서 카운트.

print(answer)