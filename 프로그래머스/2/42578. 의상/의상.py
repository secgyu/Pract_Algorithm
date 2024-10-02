from collections import Counter

def solution(clothes):
    cnt = Counter([type for _, type in clothes])

    combination = 1
    for count in cnt.values():
        combination *= (count + 1)
    
    return combination - 1