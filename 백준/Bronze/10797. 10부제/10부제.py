date_digit = int(input())

car_numbers = list(map(int, input().split()))

violation_count = 0

for number in car_numbers:
    if number == date_digit:
        violation_count += 1

print(violation_count)
