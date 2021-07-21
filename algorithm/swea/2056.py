month_dic = {
    "01": 31,
    "02": 28,
    "03": 31,
    "04": 31,
    "05": 31,
    "06": 30,
    "07": 31,
    "08": 31,
    "09": 30,
    "10": 31,
    "11": 30,
    "12": 31,
}

n = int(input())

for i in range(1, n + 1):
    calender = input()
    y, m, d = calender[:4], calender[4:6], calender[6:]
    if m not in month_dic.keys():
        print(f"#{i} -1")
        continue
    elif int(d) > month_dic[m]:
        print(f"#{i} -1")
    else:
        print(f"#{i} {y}/{m}/{d}")
