# 백준 알고리즘 - 4673 셀프넘버
# https://www.acmicpc.net/problem/4673
# 시도 횟수 : 0
# 실패 : 0
# 통과 : 0


def selfNumber ():
    creator = []
    for i in range(10001):
        Temp = i
        for j in str(i):
            Temp += int(j)
        if Temp not in creator:
            creator.append(Temp)
        if i not in creator:
            print(i)

selfNumber()