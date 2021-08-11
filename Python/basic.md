## Python 기본 문법

### 코드 라인

문장(statement)은 파이썬이 실행 가능(executable)한 최소한의 코드 단위입니다.

- 파이썬 코드는 '1줄에 1문장(statment)'이 원칙입니다.
- 기본적으로 파이썬에서는 `;`을 작성하지 않습니다.
- 한 줄로 표기할때는 `;`을 작성하여 표기할 수 있습니다.

### 변수

변수는 `=`을 통해 할당(assignment) 합니다.

- 데이터 타입을 확인하기 위해서는 `type()`을 활용합니다.
- 값의 메모리 주소를 확인하기 위해서는 `id()`를 활용합니다.

### 식별자(Identifiers)

변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름(name)입니다.

- 첫 글자에 숫자가 올 수 없으며, 대소문자(case)를 구별합니다.
- [스타일 가이드](https://www.python.org/dev/peps/pep-0008/)
- 아래의 키워드는 사용할 수 없습니다.

```
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

[파이썬 문서](https://docs.python.org/ko/3/reference/lexical_analysis.html#keywords)

## 데이터 타입

### Number TYPE

Python3에서는 `long` 타입은 없고 모두 `int` 타입으로 표기 됩니다.

- 보통 프로그래밍 언어 및 Python2에서의 long은 OS 기준 32/64비트입니다.
- Python3에서는 모두 int로 통합되었습니다.

> **오버플로우(overflow)**
>
> - 표현할 수 있는 수의 범위를 넘어가는 연산을 하게 되면, 기대했던 값이 출력되지 않는 현상, 즉 메모리를 넘어선 상황을 의미합니다.
> - 파이썬 3에서는 long 타입이 없어지고 int 타입만 남았는데, 이 int가 arbitrary precision을 지원하여 오버플로우가 발생하지 않게 되었습니다.
>   **파이썬3에서도 pydata stack을 사용하는 numpy/pandas 같은 패키지를 사용할 때는 C 스타일이 유지되기 때문에 오버플로우 발생을 고려해야 한다.**

> **임의 정밀도 산술(arbitrary-precision arithmetic)**
>
> - 사용할 수 있는 메모리양이 정해져 있는 기존의 방식과 달리, 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태를 의미합니다.
> - 특정 값을 나타내는데 4바이트가 부족하다면 5바이트, 더 부족하면 6바이트까지 사용할 수 있게 유동적으로 운용합니다.

### Float TYPE

실수는 `float`로 표현됩니다.

- 컴퓨터가 2진수(비트)를 통해 숫자를 표현하는 과정에서 부동소수점을 사용하며, 항상 같은 값으로 일치되지 않습니다. (floating point rounding error)
- 값을 같은지 비교하는 과정에서 문제가 발생할 수 있습니다.

### String TYPE

- 문자열을 묶을 때 동일한 문장부호를 활용해야하며, `PEP-8`에서는 **하나의 문장부호를 선택**하여 유지하도록 하고 있습니다.

### Boolean TYPE

파이썬에는 `True`와 `False`로 이뤄진 `bool` 타입이 있습니다.

다음은 `False`로 변환됩니다.

```
0, 0.0, (), [], {}, '', None
```

## 형변환(Type conversion, Typecasting)

파이썬에서 데이터타입은 서로 변환할 수 있습니다.

- 암시적 형변환
- 명시적 형변환

### 암시적 형변환(Implicit Type Conversion)

사용자가 의도하지 않았지만, 파이썬 내부적으로 자동으로 형변환 하는 경우입니다.
아래의 상황에서만 가능합니다.

- bool
- Numbers (int, float, complex)

## 논리 연산자

| 연산자  | 내용                         |
| ------- | ---------------------------- |
| a and b | a와 b 모두 True시만 True     |
| a or b  | a 와 b 모두 False시만 False  |
| not a   | True -> False, False -> True |

우리가 보통 알고 있는 `&` `|`은 파이썬에서 비트 연산자입니다.

- 파이썬에서 and는 a가 거짓이면 a를 리턴하고, 참이면 b를 리턴합니다.
- 파이썬에서 or은 a가 참이면 a를 리턴하고, 거짓이면 b를 리턴합니다.
- `and` 는 둘 다 True일 경우만 True이기 때문에 첫번째 값이 True라도 두번째 값을 확인해야 하기 때문에 'b'가 반환됩니다.
- `or` 는 하나만 True라도 True이기 때문에 True를 만나면 해당 값을 바로 반환합니다.

# 시퀀스(sequence)형 컨테이너

`시퀀스`는 데이터가 순서대로 나열된(ordered) 형식을 나타냅니다.

## 특징

1. 순서를 가질 수 있습니다.
2. **특정 위치의 데이터를 가리킬 수 있습니다.**

- 리스트(list)
- 튜플(tuple)
- 레인지(range)
- _문자형(string)_
- _바이너리(binary)_

# 비 시퀀스형(Non-sequence) 컨테이너

- 세트(set)
- 딕셔너리(dictionary)

### 변경 가능한(`mutable`) 데이터

- `list`
- `dict`
- `set`
