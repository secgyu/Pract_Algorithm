x = []
y = []

for i in range(3):
    X, Y = map(int, input().split())
    x.append(X)
    y.append(Y)

for i in range(3):
    if x.count(x[i]) == 1:
        x4 = x[i]
    if y.count(y[i]) == 1:
        y4 = y[i]

print(x4, y4)
