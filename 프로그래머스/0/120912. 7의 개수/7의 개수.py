def solution(array):
    count = 0

    for i in map(str, array):
        count += i.count('7')
    return count ##