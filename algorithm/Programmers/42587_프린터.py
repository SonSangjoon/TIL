from collections import deque

def solution(priorities, location):
    answer = 0
    lst = list(enumerate(priorities))
    
    dq = deque(lst)
    while dq:
        cur = dq.popleft()
        print(cur)
        print(dq)
        if any(cur[1] < pri[1] for pri in dq):
            dq.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                break

    return answer

# from collections import deque

# def solution(priorities, location):
#     answer = 0
#     lst = list(enumerate(priorities))
    
#     dq = deque(lst)
#     while dq:
#         cur = dq.popleft()
#         # if any(cur[1] < pri[1] for pri in dq):
#         #     dq.append(cur)
#         if cur[1] > max(dq, key=lambda x: x[1])[1]:
#             dq.append(cur)
        
#         else:
#             answer += 1
#             if cur[0] == location:
#                 break

#     return answer
    


# print(solution([1, 1, 9, 1, 1, 1], 0))
