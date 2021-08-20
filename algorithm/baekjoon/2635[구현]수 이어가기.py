def get_nums(n: int, i: int):  # 리스트 개수 함수
    lst = [n, i]
    while True:
        num = lst[-2] - lst[-1]
        if num >= 0:
            lst.append(num)
        else:
            break

    return lst


n = int(input())

ans = 0
for i in range(n + 1):
    temp_lst = get_nums(n, i)
    if len(temp_lst) > ans:
        ans, ans_lst = len(temp_lst), temp_lst

print(ans)
print(*ans_lst)