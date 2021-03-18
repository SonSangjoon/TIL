# Pandas
구조화된 데이터를 효과적으로 처리하고 저장할 수 있는 파이썬 라이브러리
.Array 계산에 특화된 numpy기반으로 만들어져 다양한 기능을 제공한다

```
import pandas as pd

#series: numpy array가 보강된 형태(data와 index를 가지고 있다)

data = pd.series([1,2,3,4], index['a','b','c','d'])
# 인덱스로 접근이 가능하다
data['c']
# 2

# 딕셔너리로도 만들 수 있다
```

# DataFrame 새 데이터 추가 및 수정
- 리스트로 추가하는 방법 / 딕셔너리로 추가하는 방법
- 새로운 칼럼 추가

# Indexing / Slicing

- loc : 명시적인 인덱스를 참조하는 인덱싱. 슬라이싱
- iloc: 파이썬 스타일 정수 인덱스 인덱싱, 슬라이싱

```
dataframe.loc[행의번호, 칼람명] = '바꿀 값'
```

# 누락된 데이터 처리
```
dataframe.dropna()
dataframe['칼럼'] = dataframe['칼럼'].fillna('word')
#빈 값을 word로 치환한다

A = pd.Series([2,4,6], index=[0,1,2])
B = pd.Series([1,3,5], index=[1,2,3])
A + B
A.add(B, fill_value=0)
->빈 값을 0으로 하여 계산
```