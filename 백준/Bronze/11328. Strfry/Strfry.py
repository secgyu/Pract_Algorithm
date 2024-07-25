num = int(input())

for _ in range(num):
    a, b = map(str, input().split())
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    if len(a) != len(b) :
        print("Impossible")
        continue
    for i in range(len(a)):
        if a[i] != b[i]:
            temp = "F"
            break
        else:
            temp = "T"
    if temp == "F":
        print("Impossible")
    else:
        print("Possible")