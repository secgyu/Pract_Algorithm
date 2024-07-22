card = list(range(1, 21))

for _ in range(10):
    a, b = map(int, input().split())
    card[a-1:b] = reversed(card[a-1: b])
print(" ".join(map(str, card)))
