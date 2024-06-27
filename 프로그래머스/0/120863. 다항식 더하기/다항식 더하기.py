def solution(polynomial):
    num = 0
    const = 0

    for i in polynomial.split(' + '):
        if i.isdigit():
            const += int(i)
        else:
            if i == 'x':
                i = '1x'
            num += int(i[:-1])

    if num == 0:
        return str(const)
    elif num == 1:
        return 'x + ' + str(const) if const != 0 else 'x'
    else:
        return f'{num}x + {const}' if const != 0 else f'{num}x' #