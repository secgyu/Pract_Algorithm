n, m = map(int, input().split())
array = list(map(int, input().split()))

result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if array[i] + array[j] + array[k] > m:
                continue
            else:
                result = max(result, array[i]+array[j]+array[k])
print(result)
