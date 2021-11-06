# 백준 알고리즘 - 4344 평균은 넘겠지
# https://www.acmicpc.net/problem/4344
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
C = int(sys.stdin.readline().strip())

for i in range(C):
    TestCase = list(map(int, sys.stdin.readline().split()))
    equal = sum(TestCase[1:])/TestCase[0]
        
