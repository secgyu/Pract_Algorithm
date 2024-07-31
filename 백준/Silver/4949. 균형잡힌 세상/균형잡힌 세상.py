def balance(n):
    stack = []
    for i in n:
        if i in '([':
            stack.append(i)
        elif i in ')]':
            if not stack:
                return False
            t = stack.pop()
            if (i == ')' and t != '(') or (i == ']' and t != '['):
                return False
    return not stack


while True:
    string = input()
    if string == ".":
        break
    if balance(string):
        print("yes")
    else:
        print("no")
