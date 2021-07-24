def check_balance(lst: list):
    opener = ["(", "["]
    closer = [")", "]"]
    text_stack = []

    while lst:
        e = lst.pop()
        if e in closer:
            text_stack.append(e)
        elif e in opener:
            if not text_stack:
                return "no"

            if e == "(":
                if text_stack[-1] == ")":
                    text_stack.pop()
                else:
                    return "no"

            if e == "[":
                if text_stack[-1] == "]":
                    text_stack.pop()
                else:
                    return "no"
    if text_stack:
        return "no"

    return "yes"


def balance_world():
    text_lst = []
    ans = []
    while True:
        line = input()
        if line == ".":
            break
        text_lst.append(list(line))

    for text in text_lst:
        ans.append(check_balance(text))

    return "\n".join(ans)


print(balance_world())