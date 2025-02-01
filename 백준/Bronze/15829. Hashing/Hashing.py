def hashing_function(l, string):
    r = 31
    M = 1234567891
    hash_value = 0

    for i in range(l):
        char_value = ord(string[i]) - ord('a') + 1  # a=1, b=2, ..., z=26
        hash_value += char_value * (r ** i)

    return hash_value % M

# 입력 받기
l = int(input())  # 문자열 길이
string = input().strip()  # 문자열 입력

# 해시 값 계산 및 출력
print(hashing_function(l, string))
