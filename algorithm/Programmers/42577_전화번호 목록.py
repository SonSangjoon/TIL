#런타임 에러

# from collections import defaultdict

# def solution(phone_book):
#     answer = True
#     len_dict = defaultdict(list)

#     for i in phone_book:
#         key = len(i)
#         len_dict[key].append(i)
    
#     if len(len_dict.keys()) == 1:
#         return True
    
    
#     for key, values in len_dict.items():
#         for k, v in len_dict.items():
#             if key < k:
#                 for nums in values:
#                     for n in v:
#                         if n.startswith(nums):
#                             return False
    
#     return True


def solution(phone_book):
    answer = True

    phone_book.sort(key=lambda x:x)
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]) :
            return False
                
    return True