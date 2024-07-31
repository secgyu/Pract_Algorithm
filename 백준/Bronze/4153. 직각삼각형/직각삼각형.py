import sys
input = sys.stdin.read

data = input().split()
i = 0
while True:
    a = int(data[i])
    b = int(data[i+1])
    c = int(data[i+2])
    i += 3
    if a == 0 and b == 0 and c == 0:
        break
    sides = [a, b, c]
    sides.sort()
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("right")
    else:
        print("wrong")
