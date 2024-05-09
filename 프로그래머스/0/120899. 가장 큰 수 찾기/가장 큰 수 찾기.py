def solution(array):
    max_value = max(array)
    max_index = array.index(max_value)
    
    return [max_value, max_index]