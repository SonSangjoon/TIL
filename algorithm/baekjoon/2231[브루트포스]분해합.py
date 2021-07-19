def decomposition(n):
    for i in range(n):
        num = sum(list(int(i) for i in list(str(i)))) + i
        if num == n:
            return i
    return 0


n = int(input())
print(decomposition(n))