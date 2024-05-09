import math
def solution(my_string):
    character = ''
    
    for i in my_string:
        if i.isdigit():
            character+=i
    
    total_sum = sum(int(num) for num in character)
    
    return total_sum