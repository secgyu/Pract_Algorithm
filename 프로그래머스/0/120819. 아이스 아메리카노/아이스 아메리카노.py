def solution(money):
    answer = []
    coffee = 5500
    m = money // coffee
    r = money % coffee
    answer.append(m)
    answer.append(r)
    return answer