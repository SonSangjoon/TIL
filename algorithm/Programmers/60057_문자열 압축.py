def solution(s):
    str_len = len(s)
    ans = [str_len]

    for size in range(str_len // 2, 0, -1):
        unit_lst = [s[i : i + size] for i in range(0, str_len, size)]
        stack = [[unit_lst[0], 1]]
        print(stack)
        for unit in unit_lst[1:]:
            print(unit)
            if stack[-1][0] != unit:
                stack.append([unit, 1])
            else:
                stack[-1][1] += 1
            print(stack)
        answer = ("").join([str(cnt) + wrd if cnt > 1 else wrd for wrd, cnt in stack])
        ans.append(len(answer))

    return min(ans)

print(solution("abcabcdede"))