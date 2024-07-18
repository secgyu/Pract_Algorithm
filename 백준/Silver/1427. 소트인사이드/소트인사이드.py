num = list(map(int, input()))
num.sort()
reverse_num = num[::-1]
print("".join(map(str, reverse_num)))
