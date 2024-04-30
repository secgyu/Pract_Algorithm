def solution(num_list):
    jjak = 0
    hol = 0
    answer = []
    for i in num_list:
        if i % 2 == 0:
            jjak += 1
        else:
            hol += 1
    answer.append(jjak)
    answer.append(hol)
    return answer