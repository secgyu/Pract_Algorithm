def d(n):
    result = n
    while n > 0:
        result += n % 10
        n //= 10
    return result

max_limit = 10000
generated_numbers = set()

for i in range(1, max_limit + 1):
    generated_numbers.add(d(i))

for i in range(1, max_limit + 1):
    if i not in generated_numbers:
        print(i)