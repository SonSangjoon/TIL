import math

def solution():
    X, Y = map(int, input().split())
    Z = math.floor((Y*100)/X)

    s,e = 0,10**9
    while s < e:
        m = (s+e)//2
        z = math.floor(((Y+m)*100)/(X+m))

        if z > Z:
            e = m 
        else:
            s = m + 1

    if math.floor(((Y+m+1)*100)/(X+m+1)) != Z :
        return e
    else:
        return -1

print(solution())
