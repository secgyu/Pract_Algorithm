n = int(input())

students = []

for _ in range(n):
    data = input().split()
    name = data[0]
    day, month, year = map(int, data[1:])
    students.append((year, month, day, name))

students.sort()

old = students[0][3]
young = students[-1][3]

print(young)
print(old)
