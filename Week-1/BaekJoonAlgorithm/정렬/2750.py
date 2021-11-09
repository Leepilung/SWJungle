# 백준 알고리즘 - 2750 수 정렬하기
# https://www.acmicpc.net/problem/2750
# 시도 횟수 : 1
# 실패 : 0
# 통과 :  1
import sys

N = int(sys.stdin.readline().strip())
bucket = []
for i in range(N):
    bucket.append(int(sys.stdin.readline().strip()))

for i in range(1, len(bucket)):
    for j in range(i,0,-1):
        if bucket[j] < bucket[j-1]:
            bucket[j], bucket[j-1] = bucket[j-1],bucket[j]

for i in bucket:
    print(i)