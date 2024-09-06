def solution(s):
    answer = []
    count = 0
    zero_count = 0

    while True:
        if s == "1":
            break
        zero_count += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        count += 1
    answer = [count, zero_count]
    return answer