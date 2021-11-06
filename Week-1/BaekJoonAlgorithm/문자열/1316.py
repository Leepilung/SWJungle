# 백준 알고리즘 - 1316 그룹 단어 체커
# https://www.acmicpc.net/problem/1316
# 시도 횟수 : 1
# 실패 : 0
# 통과 : 1

# 문자의 연속성 파악
# 이전 문자와 현재 문자의 정보를 비교, 바뀐 문자는 별도로 저장. 
import sys
N = int(sys.stdin.readline().strip())
count = 0
for i in range(N):
    Check = []
    prev = 0
    Text = sys.stdin.readline().strip()

    for i in Text:
        if i != prev and i not in Check:
            prev = i
            Check.append(prev)
            continue
        elif i != prev and i in Check:
            count +=1
            break
        elif i == prev and i in Check:
            continue
        else: continue # i == prev

print(N-count)
