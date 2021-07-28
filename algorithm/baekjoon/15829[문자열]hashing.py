l = int(input())
word = input()
r, m = 31, 1234567891

ans = 0

for i in range(l):
    ans += (ord(word[i]) - 96) * (r ** i)

ans %= m

print(ans)
