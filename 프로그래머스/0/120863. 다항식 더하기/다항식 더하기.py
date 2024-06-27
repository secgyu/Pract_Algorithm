def solution(polynomial):
    num = 0 
    const = 0  
    terms = polynomial.split(' + ')
    
    for term in terms:
        if 'x' in term:
            if term == 'x':
                num += 1
            else: num += int(term[:-1])
        else: const += int(term)
    
    if num == 0: return str(const)
    elif num == 1: result = 'x'
    else: result = f'{num}x'
    
    if const != 0:
        result += f' + {const}'
    
    return result
