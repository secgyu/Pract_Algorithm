n = int(input())
seq = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1
possible = True

for num in seq:
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break

if possible:
    for op in result:
        print(op)
else:
    print('NO')