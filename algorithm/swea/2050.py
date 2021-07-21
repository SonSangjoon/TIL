alphabet_lst = list(input())

for alphabet in alphabet_lst:
    num = ord(alphabet.upper()) - 64
    print(num, end=" ")