a, b = input().split()

win_dct = {"1": "3", "2": "1", "3": "2"}

if win_dct[a] == b:
    print("A")
else:
    print("B")
