## sys.stdin.readeline

```
import sys  
sys.stdin.readline(n)
```

sys.stdin.readline() > raw_input() > input() 의
입출력 속도를 가진다

```
number = sys.stdin.readline(3) # 입력 : 1234
print(number) # 결과 : 123
```
사용자의 입력도 받지만 개행 문자도 입력을 받을 수 있다.
또한 입력의 크기에 제한을 둘 수 있다.


## sys.setrecursionlimit

```
import sys  
sys.setrecursionlimit(10**8)
```

재귀 허용 깊이를 수동으로 늘려주 종종 생기는 런타임 오류를 해결한다.



## Python zip

```
Num = [1,2,3,4]
alpha = ['a','b','c','d']

lst =  list(zip(Number,alpha))
dic = {}
for num , alpha in zip(Number,Name): 
    dic[num] = alpha

print(lst)
print(dic)

결과 : 
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
{1 : 'a',2 : 'b' ,3 : 'c' ,4 : 'd'}
```

파이썬의 내장함수인 zip()은 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수이다.