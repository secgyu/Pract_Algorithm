def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n+1)
        else :
            bin_x = list('0' + bin(n)[2:])
            idx = ''.join(bin_x).rfind('0')
            bin_x[idx] = '1'
            bin_x[idx+1] = '0'
            num = int(''.join(bin_x), 2)
            answer.append(num)
    return answer