# 백준 알고리즘 - 1978 소수찾기
# https://www.acmicpc.net/problem/1978
# 시도 횟수 : 6
# 실패 : 5
# 통과 : 1

# 소수 특징 -> 1보다 큰 수 중에 1과 자기 자신만으로 나눠지면 소수. 찾은 소수의 배수는 또 제외시켜야함.
import sys
N = int(sys.stdin.readline().strip()) # 4 
Nums = list(map(int,sys.stdin.readline().strip().split())) # 1 3 5 7 출력

primeNumber = 0

# 소수 = 1과 자기 자신만으로 나뉘어야 함 -> 그전에 나눠지면 끝.
for i in Nums:
    count = 0
    if i == 1: continue
    if i > 0:
        for j in range(2,i):
            if i % j == 0:
                count +=1
        if count == 0:
            primeNumber += 1

print(primeNumber)