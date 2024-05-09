def solution(numbers):
    max_num = sorted(numbers)
    max_num.reverse()
    tmp1 = max_num[0]
    tmp2 = max_num[1]
    return tmp1 * tmp2