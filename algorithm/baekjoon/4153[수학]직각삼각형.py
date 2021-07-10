lst = []
while True:
    l = list(map(int, input().split()))

    if not sum(l):
        break
    lst.append(l)


for sides in lst:

    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("right")
    else:
        print("wrong")