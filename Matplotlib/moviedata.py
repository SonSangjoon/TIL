import re
import pandas as pd
from collections import deque

movie = "TED" #영화 이름 및 txt파일명
character = "JOHN" #분석 캐릭터 이름
source_file = f"./script/{movie}.txt" 

def make_list(filename, character):
    user_to_titles = []

    with open(filename) as file:
        for line in file:
            user_to_titles.append(line)

    dq = deque(user_to_titles)
    script_data = []
    while dq:
        e = dq.popleft()

        p = re.compile(character+"\n$")
        if p.search(e) != None:
            while dq:
                script = dq.popleft()
                if re.fullmatch(script, '\n') != None:
                    break 
                else:
                    text = script.lstrip().replace('\n','')
                    if re.search('\)', text) == None and re.match('^[0-9]*.$',text) == None:
                        script_data.append(text)

    dct = {character: script_data}

    df = pd.DataFrame(dct)

    df.to_csv(f"{movie}_{character}.csv", mode='a', header=False)

    return dct 

print(make_list(source_file, character))

