def solution(s):
    list = [0]*26

    for char in s:
        list[ord(char) - ord('a')] += 1

    result = ""

    for char in s:
        if list[ord(char) - ord('a')] == 1:
            result += char
    return ''.join(sorted(result))