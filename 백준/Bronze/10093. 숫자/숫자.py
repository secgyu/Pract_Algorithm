a, b = map(int, input().split())
count = 0
arr = []

start = min(a, b)+1
end = max(a, b)

for i in range(start, end):
    count += 1
    arr.append(i)

print(count)
print(' '.join(map(str, arr)))
