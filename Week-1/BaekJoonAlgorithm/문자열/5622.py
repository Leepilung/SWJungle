# 백준 알고리즘 - 5622 다이얼
# https://www.acmicpc.net/problem/5622
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1


import sys
Text = sys.stdin.readline().strip()

# A B C -> 2의 값을 갖도록.

phone_number = { 'A' : 2, 'B' : 2 ,'C' :2, 'D' : 3,'E' : 3,'F' : 3,'G':4,'H' : 4,'I' : 4,'J':5,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,'Q':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9,'Z':9}
sum = len(Text)

for i in list(Text):
    sum += phone_number.get(i)

print(sum)