x = int(input())
i = 1
while x > i:
    x -= i
    i += 1
if i % 2 == 0:
    print(f'{x}/{i - x + 1}')
else:
    print(f'{i - x + 1}/{x}')
