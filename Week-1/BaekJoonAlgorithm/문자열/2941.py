# 백준 알고리즘 - 2941 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

import sys
T = sys.stdin.readline().strip()
# ljes=njak
Alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in Alpha:
    if i in T:
        print(i)
        T = T.replace(i,'*')
print(len(T))