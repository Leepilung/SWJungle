# 백준 알고리즘 - 1181 단어 정렬
# https://www.acmicpc.net/problem/1181
# 시도 횟수 : 2
# 실패 : 1
# 통과 : 1

import sys
N = int(sys.stdin.readline().strip())
book = []
for i in range(N):
    word = sys.stdin.readline().strip()
    if word not in book:
       book.append(word)

book.sort(key = lambda x : x)
book.sort(key = lambda x : len(x))

for i in book:
    print(i)