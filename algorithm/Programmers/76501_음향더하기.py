def solution(absolutes, signs):
    answer = 0
    total_len = len(signs)
    for i in range(total_len):
        print(signs[i])
        if signs[i] == True: signs[i] = 1
        else: signs[i] = -1

    lst = [absolutes[idx] * signs[idx]  for idx in range(total_len)]
    answer = sum(lst)
    return answer

print(solution([4,7,12], [True,False,True]))