while True:
    n = input()
    stack = []
    res = ''
    if n == '0':
        break
    else:
        for i in n:
            stack.append(i)
        for i in range(len(stack)):
            res += stack.pop()
        if res == n:
            print('yes')
        else:
            print('no')