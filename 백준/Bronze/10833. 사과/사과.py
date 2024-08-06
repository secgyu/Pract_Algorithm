N = int(input())

total_leftover_apples = 0

for _ in range(N):
    students, apples = map(int, input().split())
    leftover_apples = apples % students
    total_leftover_apples += leftover_apples

print(total_leftover_apples)
