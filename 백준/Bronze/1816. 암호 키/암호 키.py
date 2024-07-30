case = int(input())

for i in range(case):
    nums = int(input())
    tmp = 0
    for j in range(2, 1000001, 1):
        if nums % j == 0:
            break

        elif j == 1000000:
            tmp = 1
    if tmp == 1:
        print("YES")
    else:
        print("NO")
