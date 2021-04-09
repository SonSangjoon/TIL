import pandas as pd

answer_set = []

for i in range(2**13):
    answer = '0'*(12-len(format(i, 'b'))) + str(format(i, 'b'))
    answer_set.append(answer)

print(answer_set[0])

mbti_dct = {}

# 0: I T S J  1: E F N P 

for i in answer_set:
    mbti = ""
    if (int(i[0]) + int(i[3]) + int(i[6])) > 1: mbti += 'E'
    else: mbti += 'I' 
    if (int(i[1]) + int(i[2]) + int(i[7])) > 1: mbti += 'F'
    else: mbti += 'T'    
    if (int(i[4]) + int(i[5]) + int(i[10])) > 1: mbti += 'N'
    else: mbti += 'S' 
    if (int(i[8]) + int(i[9]) + int(i[11])) > 1: mbti += 'P'
    else: mbti += 'J' 
    mbti_dct[i] = mbti


print(mbti_dct)

df = pd.DataFrame.from_dict(mbti_dct, orient="index")
df.to_csv("mbti_data_set.csv")