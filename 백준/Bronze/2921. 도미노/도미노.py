N = int(input())
total_points = 0

for i in range(N + 1):
    for j in range(i, N + 1):
        total_points += i + j

print(total_points)
