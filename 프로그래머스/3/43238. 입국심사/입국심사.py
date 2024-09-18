def solution(n, times):
    left, right = 1, 10**18
    time = 0
    while left < right:
        mid = (left + right) // 2
        num = 0
        for time in times:
            num += mid // time
        
        if num >= n: right = mid
        else : left = mid+1
    return left