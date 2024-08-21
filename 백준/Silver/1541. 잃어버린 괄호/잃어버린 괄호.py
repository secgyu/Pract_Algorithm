numbers = input()

parts = numbers.split('-')

first_part = list(map(lambda x : x.split('+'), parts))

add = lambda x: sum(map(int, x))
x = list(map(add, first_part))

print(x[0] - sum(x[1:]))