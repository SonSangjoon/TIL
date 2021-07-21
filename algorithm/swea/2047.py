letter = list(input())

for l in letter:
    try:
        print(l.upper(), end="")
    except:
        print(l, end="")