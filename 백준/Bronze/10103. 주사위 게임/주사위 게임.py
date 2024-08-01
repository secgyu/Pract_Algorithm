n = int(input())
a_sum = 100
b_sum = 100

for _ in range(n):
    c, s = map(int, input().split())

    if c > s:
        b_sum = b_sum - c
    elif c < s:
        a_sum = a_sum - s
    elif c == s:
        continue
print(a_sum)
print(b_sum)
