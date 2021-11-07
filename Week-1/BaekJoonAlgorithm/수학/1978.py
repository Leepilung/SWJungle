# 백준 알고리즘 - 1978 소수찾기
# https://www.acmicpc.net/problem/1978
# 시도 횟수 : 
# 실패 : 
# 통과 : 

# 소수 특징 -> 1보다 큰 수 중에 1과 자기 자신만으로 나눠지면 소수. 찾은 소수의 배수는 또 제외시켜야함.
import sys
N = int(sys.stdin.readline().strip())
Nums = list(map(int,sys.stdin.readline().strip().split())) # 1 3 5 7 출력

sieve = [True] * N

# n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사 

m = int(N ** 0.5)
for i in range(2, m + 1):
    if sieve[i] == True:            # i가 소수인 경우
        for j in range(i+i, N, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

result = [i for i in range(2, N) if sieve[i] == True]

print(result)