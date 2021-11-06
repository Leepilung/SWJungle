# 백준 알고리즘 - 1106 평균은 넘겠지
# https://www.acmicpc.net/problem/1106
# 시도 횟수 : 3
# 실패 : 2
# 통과 : 1

# e = round(1.23456, 3) -> 안됨
# 포메팅 함수 f'{:.03}
import sys

C = int(sys.stdin.readline().strip())

for i in range(C):
    count = 0
    TestCase = list(map(int,sys.stdin.readline().rstrip().split()))
    equal = sum(TestCase[1:])/TestCase[0]
    for i in TestCase[1:]:
        if i > equal:
            count += 1
    print(f'{(count / TestCase[0])*100:.3f}%' )