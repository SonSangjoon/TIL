def check_palindrome(n):
    l = len(n)//2
    for i in range(l):
        if n[i] != n[-i-1]:
            return "no"
    return "yes"

lst = []

while True:
    n = input()
    if n == '0':
        break
    lst.append(n)

for letter in lst:
    print(check_palindrome(letter))