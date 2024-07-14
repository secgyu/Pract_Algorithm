p, q = map(int, input().split())
array = []
for i in range(1, p+1):
    if p % i == 0:
        array.append(i)

if len(array) < q:
    print(0)
else:
    print(array[q-1])
