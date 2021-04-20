def heap(lst, K, cnt):
    if len(lst) == 1:
        if lst[0] >= K:
            return cnt
        else:
            return -1

    lst.sort()

    print(lst)
    if lst[0] >= K:
        return cnt
    else:
        lst.append(lst[0] + lst[1] * 2)
        del lst[0]
        del lst[0]
        cnt += 1
        return heap(lst, K, cnt)


def solution(scoville, K):

    answer = heap(scoville, K, 0)

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))

# 런타임 에러