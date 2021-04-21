# # 런타임 에러

# def heap(lst, K, cnt):
#     if len(lst) == 1:
#         if lst[0] >= K:
#             return cnt
#         else:
#             return -1

#     lst.sort()

#     print(lst)
#     if lst[0] >= K:
#         return cnt
#     else:
#         lst.append(lst[0] + lst[1] * 2)
#         del lst[0]
#         del lst[0]
#         cnt += 1
#         return heap(lst, K, cnt)


# def solution(scoville, K):

#     answer = heap(scoville, K, 0)

#     return answer


# print(solution([1, 2, 3, 9, 10, 12], 7))


# # 런타임 에러

# from collections import deque


# def solution(scoville, K):
#     answer = 0
#     scoville.sort()

#     dq = deque(scoville)

#     # answer = heap(scoville, K, 0)
#     print(dq)
#     while dq[0] < K:
#         answer += 1
#         if len(dq) == 1:
#             return -1

#         s1 = dq.popleft()
#         s2 = dq.popleft()

#         dq.append(s1 + s2 * 2)

#     return answer


# print(solution([1, 2, 3, 9, 10, 12], 7))

import heapq


def solution(scoville, k):
    heap = []

    for num in scoville:
        heapq.heappush(heap, num)

    cnt = 0

    while heap[0] < k:

        if len(heap) == 1:
            return -1

        heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        cnt += 1

    return cnt