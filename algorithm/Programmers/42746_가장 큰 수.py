def solution(numbers):
    
    num = [str(i) for i in numbers]
    
    num.sort(key=lambda x: x*4, reverse = True)
    
    answer = ''.join(num)
    
    if int(answer) == 0:
        return "0"
    
    return answer