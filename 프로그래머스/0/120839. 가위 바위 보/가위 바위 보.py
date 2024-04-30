def solution(rsp):
    answer = ''
    for i in range(len(rsp)):
        if rsp[i] == "0":
            answer += "5"
        elif rsp[i] == "2":
            answer += "0"
        else:
            answer += "2"
    return answer