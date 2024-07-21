N, K = map(int, input().split())
arr = [0] * (N+1)
tmp = 0

for i in range(2, N+1):
    arr[i] = i

for i in range(2, N+1):
    if arr[i] == 0:
        continue
    for j in range(i, N+1, i):
        if arr[j] == 0:
            continue
        arr[j] = 0
        tmp += 1

        if tmp == K:
            print(j)
