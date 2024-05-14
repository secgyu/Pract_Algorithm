def solution(my_string):
    vowels = 'aioeuAIOEU'
    result = [char for char in my_string if char not in vowels]
    return ''.join(result)