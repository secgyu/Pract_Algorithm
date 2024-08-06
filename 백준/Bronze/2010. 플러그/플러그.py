N = int(input())

total_outlets = 0

for _ in range(N):
    outlets = int(input())
    total_outlets += outlets

max_computers = total_outlets - (N - 1)

print(max_computers)
