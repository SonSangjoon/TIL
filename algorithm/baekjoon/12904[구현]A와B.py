# from collections import deque

# def solution():
#     S = input()
#     T = input()
#     l = len(T)

#     dq = deque([S])

#     while dq:
#         e = dq. popleft()
#         if e == T:
#             return 1
        
#         if len(e) >= l:
#             continue
        
#         dq.appendleft(e+'A')
#         dq.append(e[::-1]+'B')

#     return 0

# print(solution())

def solution():
    S = input() 
    T = input()
    
    while T:
        if T[-1] == 'A':
            T = T[:-1]
        else:
            T = T[:-1]
            T = T[::-1]
        
        if T == S:
            return 1
        
        elif len(T) == len(S):
            return 0 

print(solution())