n, k = map(int, input().split())

student = {}

for i in range(1, 7):
    student[(0, i)] = 0
    student[(1, i)] = 0

for _ in range(n):
    gender, grade = map(int, input().split())
    student[(gender, grade)] += 1

total_room = 0

for key in student:
    count = student[key]

    if count % k == 0:
        total_room += count // k
    else:
        total_room += count // k + 1

print(total_room)
