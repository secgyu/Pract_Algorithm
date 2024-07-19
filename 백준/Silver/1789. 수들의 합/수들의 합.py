num = int(input())
total = 0
count = 0

while True:
    count += 1
    total += count

    if total > num:
        break
print(count-1)
