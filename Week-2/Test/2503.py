# 백준 알고리즘 - 2503 숫자 야구
# https://www.acmicpc.net/problem/2503
# 시도 횟수 : 
# 실패 : 
# 통과 : 

# 민혁이가 영수에게 몇번 질문했는지 -> 1 < N < 100
# N개의 줄마다 민혁이가 질문한 세자리 수와 영수가 답한 스트라이크, 볼 개수


import sys
from itertools import permutations, combinations

answer = []
a = [1,2,3,4,5,6,7,8,9]
Nums = list(combinations(a,3))

for num in Nums:
    Nums2 = list(permutations(num,3))  
    for num2 in Nums2:
        answer.append(list(num2))    # 3개로 된 중복없는 수 전부 배열에 삽입

N = int(sys.stdin.readline().strip())

for _ in range(N):
    Question, Strike, Ball = map(int,sys.stdin.readline().split())
    Question_list = []

    for j in str(Question):    # 질문한 값 문자열 -> 배열로 각각 확인할 수 있게 리스트화
        Question_list.append(int(j))

    for idx, i in enumerate(answer):  # answer의 값을 index= 0 와 (1 2 3) 값으로 분리하면서 반복 
        StrikeCount, BallCount = 0, 0
        for index, num in enumerate(i):   # i는 배열이므로 또다시 index와 값으로 분리 0 1, 1 2, 2 3 처럼
            if num == Question_list[index]:   # 스트라이크 자리수가 동일하면 카운트 하나 증가
                StrikeCount += 1
            elif num == Question_list[index -1] or num == Question_list[index -2]:  # 나머지 2개 검사해서 같으면 볼 카운트 증가
                BallCount += 1
        if StrikeCount != Strike or BallCount != Ball:  # 만약 같지 않으면 0 0 0으로 처리
            answer[idx] = [0,0,0]

answer_count = 0

for k in answer:
    if k != [0,0,0]:
        answer_count +=1

print(answer_count)