# 백준 알고리즘 - 9935 문자열 폭발
# https://www.acmicpc.net/problem/9935
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
import sys 
string = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

 
lastChar = bomb[-1] 
stack = []
length = len(bomb) 

for char in string:
    stack.append(char)
    if char == lastChar and ''.join(stack[-length:]) == bomb:
        del stack[-length:]

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)