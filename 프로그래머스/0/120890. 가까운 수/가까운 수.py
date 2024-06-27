def solution(array, n):
    tmp = float('inf')
    answer = None
    
    for i in array:
        m_tmp = abs(n - i)
        if m_tmp < tmp:
            tmp = m_tmp
            answer = i
        elif m_tmp == tmp:
            if i < answer:
                answer = i
    return answer
            