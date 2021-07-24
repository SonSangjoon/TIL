day, night, height = map(int, input().split())
ans, left = (height - day) // (day - night) + 1, (height - day) % (day - night)
if left:
    ans += 1
print(ans)