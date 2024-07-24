import bisect

case = int(input())

for _ in range(case):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    count_num = 0

    for i in A:
        count_num = count_num + (bisect.bisect_left(B, i))

    print(count_num)
