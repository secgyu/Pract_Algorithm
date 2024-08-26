def get_clock_number(numbers):
    rotations = []
    for i in range(4):
        rotated = int(''.join(map(str, numbers[i:] + numbers[:i])))
        rotations.append(rotated)
    return min(rotations)

numbers = list(map(int, input().split()))

clock_number = get_clock_number(numbers)

count = 0

for i in range(1111, clock_number + 1):
    if get_clock_number(list(map(int, str(i)))) == i:
        count += 1

print(count)