## 이진 탐색 알고리즘

 - 순차 탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
 - 이진 탐색: 정렬되어있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
    * 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정
    * 단계 바다 탐색 범위를 2를 나누는 것 과 동일 하므로 연산횟수는 log2N에 비례한다.


```
//재귀
def binary_search(array, target,start,end):
    if start > end:
        return None
    mid = (start +end) //2
    if array[mid] == target:
        return mind
    elif array[mid] > target:
        return binary_search(arrary, target, start, mid -1)
    else:
        return binary_search(array, target, mid + 1, end)


//반복문
def binary_search(array, target, start, end):
    while start <= end:
     mid = (start + end) // 2

     if array[mid] == target:
        return mid
    elif array[mid] > target:
        end =  mid -1
    else:
        start = mid +1
    return None
```

## 파이썬 이진 탐색 라이브러리

```

// 값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
left_index = bisect_left(a, left(value)
right_index = bisect_right(a, right_value)
 
return right_index - left_index

```

## 파라메트릭 서치
파라메트릭 서치란 최적화 문제를 결정문제로 바꾸어 해결하는 기법 :
ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화문제
일반적으로 코딩테스트에서 파라메트릭 서치문제는 이진탐색을 통해 해결할 수 있다.