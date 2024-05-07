import math

def solution(n):
    sqrt_n = int(math.sqrt(n))  
    if sqrt_n * sqrt_n == n:  
        return 1  
    else:
        return 2 
