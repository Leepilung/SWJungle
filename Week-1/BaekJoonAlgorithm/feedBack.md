# FeedBack

개인, 팀단위 피드백을 전부 기록(특정 알고리즘의 풀이 피드백이 필요한 경우 해당 문제 폴더화 시켜서 만들기)

# Python에서 input 대신 sys.stdin.readline()의 사용

입출력 속도는 다음과 같다.

```python
sys.stdin.readline() > raw_input() > input()
```

그리고 sys.stdin.readline의 사용은

```py
import sys
```

와 같이 모듈삽입이 필수적으로 선행되야하고, 입력값의 말미에 자동으로 `개행문자(\n)`가 삽입된다.

이를 제거하는 방법은 경우에따라 다른데 여러개의 변수를 입력받는 경우

```py
# 입력의 형태가 A B와 같이 공백문자를 포함하고 변수가 여러개인 경우
A, B = map(원하는 타입 형태(int,str,etc), sys.stdin.readline().split(" "))

# 변수가 한개인 경우
A = 형변환 내장함수(sys.stdin.readline().strip())
```
