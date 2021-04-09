answer_set = []

for i in range(2**13):
    answer = '0'*(13-len(format(i, 'b'))) + str(format(i, 'b'))
    answer_set.append(answer)

print(answer_set[0])

mbti_dct = {}

for i in answer_set:
    mbti = ""
    if sum([int (i) for i in i[:3]]) > 1: mbti += 'E'
    else: mbti += 'I' 
    if sum([int (i) for i in i[3:6]]) > 1: mbti += 'S'
    else: mbti += 'N'    
    if sum([int (i) for i in i[6:9]]) > 1: mbti += 'F'
    else: mbti += 'T' 
    if sum([int (i) for i in i[9:12]]) > 1: mbti += 'P'
    else: mbti += 'J' 
    mbti_dct[i] = mbti

print(mbti_dct)