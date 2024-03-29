# 백준 알고리즘 - 10809 알파벳 찾기
# https://www.acmicpc.net/problem/10809
# 시도 횟수 : 3
# 실패 : 2
# 통과 : 1

import sys
import string

alphabet = list(string.ascii_lowercase)
result = [-1 for _ in range(len(alphabet))]
S = list(sys.stdin.readline().strip())

for i in S:
    result[alphabet.index(i)] = S.index(i)

sum = ''
for i in result:
    sum += str(i)+' '
print(sum[:-1])