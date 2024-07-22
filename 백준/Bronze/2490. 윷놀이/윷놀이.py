def result(arr):
    count_0 = arr.count(0)
    if count_0 == 1:
        return 'A'
    elif count_0 == 2:
        return 'B'
    elif count_0 == 3:
        return 'C'
    elif count_0 == 4:
        return 'D'
    else:
        return 'E'


for _ in range(3):
    arr = list(map(int, input().split()))
    print(result(arr))
