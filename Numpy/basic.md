#Numpy

Numpy라이브러리는 효율적인 데이터 분석이 가능하도록 N차원의 배열 객체를 지원한다. 또한 list 보다 빠른 연산과 효율적인 메모리 사용을 가능하게 한다.
```
import numpy as np


np.zeros(5, dtype= int) #0이 들어있는 배열 생성
np.ones(5, dtype= int) #1이 들어있는 배열 생성

np.empty #초기화가 없는 배열 반환
np.arrange(n) #배열 버전의 range 함수

np.random.random((2,2)) #난수가 들어있는 배열
np.random.normal(0,1,(2,2))
np.random.randint(0,10,(2,2))
#(2,2) -> 크기의 배열을 생성


array = np.random.randint(10, size=(2,2))
array.ndin #2
array.shape #(2,2)
array.size #12
array.dtype #dtype('int64')


array.reshape(2,4) #(2,4) 형태로 모양을 바꾼다

#열의 개수가 같은 array끼리는 세로(axis 0)로 붙일 수 있고, 행의 개수가 같은 array끼리는 가로(axis 1)로 붙일 수 있다.
arrary.concatenate()

```


#브로드캐스팅

```
A = np.arange(6).reshape(6,1)
B = np.arange(6)
print(A+B)


#[[ 0  1  2  3  4  5]
 #[ 1  2  3  4  5  6]
 #[ 2  3  4  5  6  7]
 #[ 3  4  5  6  7  8]
 #[ 4  5  6  7  8  9]
 #[ 5  6  7  8  9 10]]

```

#집계함수 / 마스킹 연산

집계: 데이터에 대한 요약 통계를 볼 수 있다
마스킹 연산: True, False array를 통해서 특정 값들을 뽑아내는 방법