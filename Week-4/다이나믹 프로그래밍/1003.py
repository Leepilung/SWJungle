# 백준 알고리즘 - 1003 피보나치 함수
# https://www.acmicpc.net/problem/1003
# 시도 횟수 : 
# 실패 : 
# 통과 : 
import sys
input = sys.stdin.readline

zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print('{} {}'.format(zero[num], one[num]))

T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    fibonacci(N)