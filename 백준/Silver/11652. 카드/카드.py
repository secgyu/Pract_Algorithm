import sys
input = sys.stdin.readline

N = int(input())
dict = {}

for _ in range(N):
    card = int(input())

    if card in dict:
        dict[card] += 1
    else:
        dict[card] = 1

max_count = 0
min_number = 2**63


#   key, value
for num, count in dict.items():
    if count > max_count:
        max_count, min_number = count, num
    elif count == max_count:
        if num < min_number:
            min_number = num
print(min_number)
