def solution(my_string):
    sum = 0
    tmp = ""
    for i in my_string:
        if i.isdigit():
            tmp += i
        else:
            if tmp:
                sum += int(tmp)
                tmp = ""
    if tmp:
        sum += int(tmp)
    return sum