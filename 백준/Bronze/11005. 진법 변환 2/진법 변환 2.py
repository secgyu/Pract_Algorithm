n, b = map(int, input().split())
result = ''
while n:
    n, r = divmod(n, b)
    if r < 10:
        result += str(r)
    else:
        result += chr(r + 55)
print(result[::-1])
