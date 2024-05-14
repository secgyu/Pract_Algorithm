def solution(num, k):
    line = list(map(int, str(num)))
    for index, digit in enumerate(line):
        if digit == k:
            return index+1

    return -1