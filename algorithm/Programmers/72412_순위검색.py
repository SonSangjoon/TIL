def solution(info, query):
    answer = []
    
    info_table = []
    
    for i in info:
        info_table.append(list(map(str, i.split())))
    
    info_table.sort(key= lambda x: x[4])

    for q in query:
        cond = list(map(str, q.split()))
        cnt = 0
        print("cond:", cond[0], cond[2], cond[4], cond[6], cond[7])
        for info in info_table:
            if cond[0] != info[0] and cond[0] != '-':
                continue
            if cond[2] != info[1] and cond[2] != '-':
                continue
            if cond[4] != info[2] and cond[4] != '-':
                continue
            if cond[6] != info[3] and cond[6] != '-':
                continue
            if int(cond[7]) > int(info[4]):
                continue
            cnt += 1
        answer.append(cnt)
        
        
    return info_table
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java or backend or junior or pizza 100","python or frontend or senior or chicken 200","cpp or - or senior or pizza 250","- or backend or senior or - 150","- or - or - or chicken 100","- or - or - or - 150"]))