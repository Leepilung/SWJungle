# 백준 알고리즘 - 1157 단어 공부
# https://www.acmicpc.net/problem/1157
# 시도 횟수 : 3
# 실패 : 2
# 통과 : 1

# 왜틀렸는지 모르겠음.. 기존 사고방식, 알고리즘 전부 동일. 내장함수의 사용유무만 달랐으나 내장함수로 풀었더니 해결됨.

import sys
import string

alphabet = list(string.ascii_lowercase)
count = [0 for _ in range(len(alphabet))]


T = list(sys.stdin.readline().strip().lower())

for i in T:
    count[alphabet.index(i)] += 1

if count.count(max(count)) > 1:
    print('?')
else:
    print(alphabet[count.index(max(count))].upper())