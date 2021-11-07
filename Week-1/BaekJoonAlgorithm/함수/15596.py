# 백준 알고리즘 - 15596 정수 N개의 합
# https://www.acmicpc.net/problem/15596
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

def solve (a:list) -> int :
    sum = 0
    for i in a:
        sum += i
    return sum