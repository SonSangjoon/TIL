## 자료구조 종류
- 정수, 실수, 문자
- 배열, 해쉬, 링크드리스트
- 스택, 큐, 트리, 그래프 ...

주어진 상황에 맞는(optimized) 된 자료구조를 사용해야 한다.



## call by reference / call by value (CBV /CBR )


Python은 함수를 실행할때 Call by reference같은 느낌으로 reference를 넘겨준다. 
하지만 이때 넘겨주는 것은 변수가 담고 있는 자료(Data)의 reference이다.

자료가 mutable하다면 변경해도 reference가 보존되므로 결과적으로 Call by reference처럼 적용되는 것으로 보인다. 
자료가 immutable하다면 결과적으로 Call by value처럼 적용되는 것으로 보인다

- 숫자형 (Number) : immutable
- 문자열 (String) : immutable
- 리스트 (List) : mutable
- 튜플 (Tuple) : immutable
- 딕셔너리 (Dictionary) : mutable



## 트리 순회

```
        1
      /   \ 
    2      3
  /  \    /  \
4     5  6    7
```

- 전위 순회: 1-2-4-5-3-6-7
- 중위 순회: 4-2-5-1-6-3-7
- 후위 순회: 4-5-2-6-7-3-1

## 트리 종류
- 이진 트리: 모든 노드가 최대 2개인 트리(완전 이진 트리,포화 이진 트리)