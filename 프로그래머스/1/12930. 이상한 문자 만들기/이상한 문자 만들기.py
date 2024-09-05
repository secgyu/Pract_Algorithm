def solution(s):
    answer = ''
    new_strings = s.split(' ')
    for string in new_strings:
        for i in range(len(string)):
            if i % 2 == 0:
                answer += string[i].upper()
            else:
                answer += string[i].lower()
        answer += ' '
    return answer[:-1]