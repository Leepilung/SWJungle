# 백준 알고리즘 - 10000 원 영역
# https://www.acmicpc.net/problem/10000
# 시도 횟수 : 0
# 실패 : 0
# 통과 : 0


import sys

N = int(sys.stdin.readline())
points = []
for _ in range(N):
    x, r =list(map(int, sys.stdin.readline().split()))
    points.append(["{", x - r, 0, 0])  #괄호, 좌표, 상태(이어지면 1 아니면 0), 이어진 원 지름 길이의 합  
    points.append(["}", x + r, 0, 0])
points.sort(key=lambda x:(x[1], x[0])) 

stack = []
answer = 1

for i in range(len(points)):
    if points[i][0] == "{":
        if stack:
            if stack[-1][1] == points[i][1] or stack[-1][3] == points[i][1]:  # 스택에 마지막 좌표값과 point의 좌표값이 같거나
                # Stack 지름길이의 합이 넣을 point의 좌표값과 같으면
                stack[-1][2] = 1    # stack안에 가장 마지막 값의 상태를 1로만든다.(이어져있다)
            else:
                stack[-1][2] = 0
        stack.append(points[i])
    else:   # 입력한 position 값이 "}"와 같으면
        half = stack.pop()  # half에 stack의 마지막값을 빼와서
        if stack and stack[-1][2] == 1: # stack이 빈배열이 아니고, stack의 이어짐 유무가 1이면
            stack[-1][3] = points[i][1] # stack안의 마지막 값의 지름값을 닫는 괄호(positon의 좌표값으로 바꿈)
        if half[2] == 1 and half[3] == points[i][1]: # half의 2번값  이어진 상태가 1이고 , half의 지름값이 포지션 값의 좌표길이와 같으면
            answer += 1     #영역이 닫힌걸 의미하므로 answer 에 1 한번 더 가산
        answer += 1     # 영역이 닫혔다고 가정해야 하므로 answer에 값 1 가산
print(answer)




