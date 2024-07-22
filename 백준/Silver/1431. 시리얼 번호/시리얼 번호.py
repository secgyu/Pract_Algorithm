def sum_of_digits(s):
    return sum(int(char) for char in s if char.isdigit())

def custom_sort(serials):
    serials.sort(key=lambda x: (len(x), sum_of_digits(x), x))

n = int(input())
serials = [input().strip() for _ in range(n)]

custom_sort(serials)

for serial in serials:
    print(serial)
