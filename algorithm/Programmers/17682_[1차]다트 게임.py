https://programmers.co.kr/learn/courses/30/lessons/17682

from collections import deque

def solution(dartResult):
    dart = list(dartResult)
    answer = 0
    
    sdt = {'S': 1, 'D': 2, 'T': 3}
    spc = {'*': -1, '#': 2}
    
    lst = []
    
    for i in range(len(dart)):
        if dart[i] in sdt.keys():
            if dart[i-1] == '0' and i > 1:
                if dart[i-2] == '1':
                    lst.append(10**sdt[dart[i]])
                else:
                    lst.append(int(dart[i-1])**sdt[dart[i]])  
            else:
                lst.append(int(dart[i-1])**sdt[dart[i]])
                
        if dart[i] == '*':
            lst[-1] = lst[-1]*2
            if len(lst) >1:
                lst[-2] = lst[-2]*2
        if dart[i] == '#':
            lst[-1] = lst[-1]*(-1)
    
    answer = sum(lst)

    return answer