# lambda

```
def square(x):
    return x*x

square = lambda x: x*x

def get_split(row):
    split = row.split(',')
    return split[1]

sorted(book, key= get_split)

#lambda 함수 솰용
det_split = lambda row: row.split(',')[1]
sorted(book, key= get_split)

#축약
sorted(book, key= lambda row: row.split(',')[1])

```

# map()

- map(f, list)
- map( lambda row: row.split(','), books)
