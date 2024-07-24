import sys
input = sys.stdin.readline

student = int(input())
seq = []

for _ in range(student):
    name, korean, english, math = input().split()
    korean = int(korean)
    english = int(english)
    math = int(math)

    seq.append((name, korean, english, math))

seq.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in seq:
    print(i[0])
