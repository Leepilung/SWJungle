# make, Makefile

# make & Makefile 이란?

적백 나무등의 C프로젝트에서 Shell에서 컴파일을 하는 경우, `make` 명령어로 컴파일을 실행하였는데 이는 어떻게 작동하는 것일까?

Makefile이 있는 디렉토리에서 make만 치면 컴파일이 실행되는 이유는 `make`가 **파일 관리 유틸리티** 이기 때문이다.

`make`는 파일 간의 종속관계를 파악하여 Makefile(기술파일)에 적힌 대로 컴파일러에 명령하여 SHELL 명령이 순차적으로 실행될 수 있게 한다.

# 👍 make의 장점

1. 각 파일에 대한 반복적 명령을 자동화하여 시간을 절약할 수 있다.

2. 프로그램의 종속 구조를 빠르게 파악 할 수 있으며 관리가 용이해진다.

3. 단순 반복 작업 및 재작성을 최소화 할 수 있다.

4. 입력파일 변경 시 결과파일 자동 변경을 원할 때 지능적인 배치작업 수행이 가능하다.

5. 일일이 gcc 명령어를 안치고도 간단하면서 용이하게 컴파일을 진행할 수 있다.

# 만약 make 파일을 사용하지 않고 컴파일 한다면

> 📝 예제

<Img src=https://t1.daumcdn.net/cfile/tistory/236F9B4D56E5904C37>

## 기본적인 컴파일 과정

컴파일은 gcc를 사용한다.

1. 기본적으로 c파일에서 object파일을 생성한다.

> 명령어

```
gcc -c -o 파일명.o 파일명.c
```

여기서 -c 옵션은 object 파일을 생성하는 옵션이고,
-o 옵션은 생성 될 파일 이름을 지정하는 옵션이다.

여기서는 -o 옵션을 넣지 않아도 object 파일이름이 (c파일이름).o로 자동 생성 된다.

하지만 실행 파일 생성시 -o 옵션을 넣지 않으면 모든 파일이 a.out 이라는 이름을 가지게 되므로 여러 개의 실행 파일을 생성해야 할 때 효율적인 옵션이다.

2. 각 object 파일을 묶어 컴파일을 통해 diary_exe 실행파일 생성

```
gcc -o diary_exe 파일명1.o 파일명2.o 파일명3.o
```

위 명렁어를 실행하면 diary_exe라는 이름의 실행파일이 생성된다.(실행파일명 임의 설정 가능)

실행하려면 해당 실행 파일이 있는 경로로 이동 한 후에

```
./diary_exe
```

입력시 실행되며 함수에 입력해두었던 값(printf등)이 터미널에서 실행된다.

그러나 이러한 컴파일 과정은 파일이 많아질수록 불가능에 가까워진다.

만약 하나의 실행파일을 만드는데 필요한 c파일이 1000개, 10000개라면 일일이 명령어를 불러올 수 없는 노릇이다.

---

# make를 이용한 컴파일

우선 make를 사용하기 이전에 Makefile은 어떻게 만드는지 알아 본 후 컴파일을 진행해 보자.

## Makefile 의 구성

Makefile은 다음과 같은 구조를 가진다.

- 목적파일(Target) : 명령어가 수행되어 나온 결과를 저장할 파일

- 의존성(Dependency) : 목적파일을 만들기 위해 필요한 재료

- 명령어(Command) : 실행 되어야 할 명령어들

- 매크로(macro) : 코드를 단순화 시키기 위한 방법

## Makefile의 기본 구조

<img src=https://t1.daumcdn.net/cfile/tistory/242A274956E5920F2B>

## Makefile 작성 규칙

```
목표파일 : 목표파일을 만드는데 필요한 구성요소들
(tab)목표를 달성하기 위한 명령 1
(tab)목표를 달성하기 위한 명령 2
```

매크로 정의 : `Makefile`에 정의한 string 으로 치환한다.

명령어의 시작은 반드시 탭으로 시작한다.

Dependency가없는 target도 사용 가능하다.

> 📝 예제

Makefile을 만들어 보자

```c
// Makefile 파일을 만들고 아래와 같이 입력해보자.
diary_exe : memo.o calendar.o main.o
		gcc -o diary_exe memo.o calendar.o main.o

memo.o : memo.c
		gcc -c -o memo.o memo.c

calendar.o : calendar.c
		gcc -c -o calendar.o calendar.c

clean :
		rm *.o diary_exe
```

이 후에 해당 경로에서 make clean을 입력하면 .o확장자 파일과 diary_exe파일이 삭제되고

make 명령어를 입력하면 위에 입력해놓은 대로 .o파일을 생성한다.

## Makefile 개선 -> 매크로

매크로는 생각보다 간단하다. 위 Makefile에서 중복되는 파일 이름들을 특정 단어로 치환하면 된다.

C언어에서 #define을 하는 것과 비슷한 원리이다.

> 📝 예제

```c
CC = gcc
CFLAGS = -W -WALL
TARGET = diary_exe

$(TARGET) : memo.o calendar.o main.o
		$(CC)	$(CFLAGS) -o $(TARGET) memo.o calendar.o main.o

memo.o : memo.c
		$(CC)	$(CFLAGS) -c -o memo.o memo.c

calendar.o : calendar.c
		$(CC)	$(CFLAGS) -c -o calendar.o calendar.c

main.o : main.c
		$(CC)	$(CFLAGS) -c -o main.o main.c

clean :
		rm *.o diary_exe
```

> 🏷 작성 규칙

1. 매크로를 참조 할 때는 소괄호나 중괄호 둘러싸고 앞에 ‘$’를 붙인다.

2. 탭으로 시작해서는 안되고 , :,=,#,”” 등은 매크로 이름에 사용할 수 없다.

3. 매크로는 반드시 치환될 위치보다 먼저 정의 되어야 한다.

여기서 -W -Wall는 컴파일 시 컴파일이 되지 않을 정도의 오류라도 모두 출력되게 하는 옵션이다.

```C
make clean
vi Makefile //매크로 사용 예제처럼 수정
./diary_exe
```

이전과 같은 결과가 나와야 한다.

## Makefile 개선하기2 : 내부 매크로 사용

> 📝 예제

```c
// Makefile 내부 코드
CC = gcc
CFLAGS = -W -WALL
TARGET = diary_exe
OBJECTS = memo.o main.o calendar.o

all : $(TARGET)

$(TARGET) : $(OBJECTS)
		$(CC)	$(CFLAGS) -o $@ $^

clean :
		rm *.o diary_exe
```

내부 매크로를 사용하면 코드가 더 단순해 짐을 알 수 있다.

여기서 사용된 내부 매크로는 다음과 같은 기능을 한다.

```c
* “$@” : 현재 타겟의 이름
* “$^” : 현재 타겟의 종속 항목 리스트
```

위 코드를 한번 처음부터 끝까지 해석해 보자.

1. gcc 컴파일러를 이용

2. 사소한 오류까지 출력

3. 최종 타겟 파일은 diary_exe

4. OBJECT 로 정의할 파일들은 memo.o main.o calendar.o

5. all 은 현재는 사용하지 않았지만 타겟 파일이 여러개 일때 사용됩니다.

6. 타겟 파일을 만들기 위해 OBJECT 들을 사용한다.( 단 OBJECT 파일이 없다면 OBJECT 파일과 이름이 동일한 C파일을 찾아 OBJECT파일을 생성한다. )

7. gcc -o diary_exe memo.o main.o calendar.o과 동일

8. 더미타겟
