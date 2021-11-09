# 백준 알고리즘 - 10989 도수 정렬
# https://www.acmicpc.net/problem/10989
# 시도 횟수 : 
# 실패 : 
# 통과 : 
import os
import sys

N = int(sys.stdin.readline().strip())
bucket = [0]*10001
for i in range(N):
    bucket[int(sys.stdin.readline().strip())] +=1 # 입력값 변수할당하니까 통과못함.

def Csort(a):
    for i in range(1,len(bucket)):
        if bucket[i] != 0:
            for _ in range(1,bucket[i]+1):
                print(i)

Csort(bucket)
