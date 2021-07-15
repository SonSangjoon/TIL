n = int(input())
lst = sorted([int(input()) for _ in range(n)])
str_lst = [str(int) for int in lst]
print("\n".join(str_lst))