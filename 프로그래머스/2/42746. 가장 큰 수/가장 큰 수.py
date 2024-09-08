from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)))
    result = ''.join(numbers)
    # 모든 숫자가 '0'일 경우 '0' 하나만 반환
    return '0' if result[0] == '0' else result
