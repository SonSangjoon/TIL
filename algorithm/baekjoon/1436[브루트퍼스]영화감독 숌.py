n = int(input())
ans = 0
num = 666
while True:
    if "666" in str(num):
        ans += 1
        if ans == n:
            print(num)
            break
    num += 1
