def solution(i, j, k):
    str_k = str(k)
    count = 0
    for number in range(i, j+1):
        str_number = str(number)
        count += str_number.count(str_k)
    return count

