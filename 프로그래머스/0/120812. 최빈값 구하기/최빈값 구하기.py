def solution(array):
    answer = []
    dic = {}
    for i in array:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    max_val = max(dic.values())
    for key,val in dic.items():
        if val == max_val:
            answer.append(key)
    if len(answer) == 1:
        return answer[0]
    else:
        return -1