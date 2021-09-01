import sys

n = int(sys.stdin.readline())
s = set()

for _ in range(n):
    temp = sys.stdin.readline().strip().split()

    if len(temp) == 1:
        func = temp[0]
        if func == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()

    else:
        func, num = temp[0], temp[1]
        num = int(num)
        if func == "add":
            s.add(num)
        elif func == "remove":
            s.discard(num)
        elif func == "check":
            print(1 if num in s else 0)
        elif func == "toggle":
            if num in s:
                s.discard(num)
            else:
                s.add(num)