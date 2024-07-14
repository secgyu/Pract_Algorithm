M = int(input())
N = int(input())

array = []

for i in range(M, N+1):
    count = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            array.append(i)

if len(array) < 1:
    print(-1)
else:
    print(sum(array))
    print(min(array))
