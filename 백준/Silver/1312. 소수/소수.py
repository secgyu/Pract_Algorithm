A, B, N = map(int, input().split())
A %= B

for _ in range(N):
    A *= 10
    digit = A // B
    A %= B
print(digit)