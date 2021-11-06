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

## 모듈

> string 모듈

```py
# 알파벳 소문자 리스트화하여 나열
list(string.ascii_lowercase)
# 알파벳 대문자 리스트화하여 나열
list(string.ascii_uppercase)
# 알파벳 소문자 대문자 전부 포함하여 나열
list(string.ascii_letters)
```

## 리스트

> 리스트의 특정 인덱스값 찾기

list = [1,2,3,4] 라고하면

3이라는 값의 인덱스를 찾고싶다면 `list.index(3)`과 같이 사용하면 된다.

> 리스트의 특정 인덱스값 갯수 구하기

```py
list = [1,2,3,4,3,4]
# 3의 갯수를 찾고싶으면
list.count(3)
```

## try, except 문

try문을 수행하다 에러가 발생시

excpet문으로 떨어짐.

## 포메팅 함수

> 소수점 표현

1. round 함수

   ```py
   round(반올림하고자 하는 값, 자릿수)
   ```

2. 파이썬 format 서식 지정으로 소수점 관리

   ```py
   # "이것을 문자열 { : .2f}".format(실수 입력)
   a = "format example1 : {:.2f}".format(1.23456789)
   print(a) # 1.23 출력
   ```

3. 파이썬 f-string에서 소수점 관리

   ```py
   num1 = 1.23456789
   num2 = 9.87654321
   print(f'f-string example1 : {num1:.0f}') # 1
   print(f'f-string example2 : {num1:.1f}') # 1.2
   print(f'f-string example3 : {num1:.2f}') # 1.23
   print(f'f-string example4 : {num1:.3f}') # 1.235
   print(f'f-string example5 : {num1:.4f}') # 1.2346
   ```

## 딕셔너리

> 다음 형태의 딕셔너리 1:1로 매칭해서 값 부여하는 방법.

```py
Number = { 3 : ['a','b','c'], 4 : ['d','e','f'], 5 : ['g','h','i'],
6 : ['j','k','l'], 7 : ['m','n','o'], 8 : ['p','q','r','s'],
9 : ['t','u','v'], 10 : ['w','x','y','z'] }

for key, value in Number.items():
    print(key,value)
# 출력되는 값
#key     value
# 3 ['a', 'b', 'c']
# 4 ['d', 'e', 'f']
# 5 ['g', 'h', 'i']
# 6 ['j', 'k', 'l']
# 7 ['m', 'n', 'o']
# 8 ['p', 'q', 'r', 's']
# 9 ['t', 'u', 'v']
# 10 ['w', 'x', 'y', 'z']
```

- 활용 방법 -> 찾으려는 값이 value안에 있으면 key를 결과값에 가산해주는 식으로 하면됨.
