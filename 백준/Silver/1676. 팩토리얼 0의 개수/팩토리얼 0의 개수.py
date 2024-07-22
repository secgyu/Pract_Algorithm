number = int(input())
count = 0

while number >= 5:
    number //= 5
    count += number

print(count)
