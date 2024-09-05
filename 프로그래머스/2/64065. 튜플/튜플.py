def solution(s):
    answer = []
    s = s.lstrip('{').rstrip('}').split('},{')
    s = [set(map(int, x.split(','))) for x in s]
    s.sort(key=len)
    prev_set = set()

    for current_set in s :
        new_element = list(current_set - prev_set)[0]
        answer.append(new_element)
        prev_set = current_set
    return answer
