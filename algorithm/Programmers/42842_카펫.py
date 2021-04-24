def solution(brown, yellow):
    answer = []
    
    s = brown + yellow
    
    for i in range(1, s+1):
        if s % i == 0 and (i-2)*(s//i-2) == yellow:
            answer.append(s//i)
            answer.append(i)
            break


    return answer