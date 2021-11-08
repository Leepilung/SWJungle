# 백준 알고리즘 - 9020 골드바흐
# https://www.acmicpc.net/problem/9020
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1
import sys
T = int(sys.stdin.readline().strip())

def Eratos_sieve(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           
            for j in range(i+i, n, i): 
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

primeNumber = Eratos_sieve(10000)

for i in range(T):
    goldbach = int(sys.stdin.readline().strip())
    goldbach_list = []

    for i in primeNumber:
        for j in primeNumber:
            if i + j > goldbach:
                break
            if i + j == goldbach:
                goldbach_list.append([i,j])
                break
    min = 100000
    answer_i = 0
    answer_j = 0
    for i,j in goldbach_list:
        if abs(i-j) < min:
            min = abs(i-j)
            answer_i = i
            answer_j = j
    
    print('{0} {1}'.format(answer_i,answer_j))