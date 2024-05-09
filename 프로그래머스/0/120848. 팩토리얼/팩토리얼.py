def solution(n):
    if n < 1:
        return 0
    
    factorial = 1
    i = 1
    while factorial <= n:
        i += 1
        factorial *= i
        
        if factorial > n:
            return i -1
    return i