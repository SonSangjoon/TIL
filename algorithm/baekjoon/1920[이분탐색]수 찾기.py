n = input()
lst_n = set(input().split())
m = input()
lst_m = list(input().split())

for num in lst_m:
    print(1) if num in lst_n else print(0)
