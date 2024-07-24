import math


def escape(n):
    return int(math.sqrt(n))


case = int(input())
seq = []
for _ in range(case):
    room = int(input())
    seq.append(escape(room))

for i in seq:
    print(i)
