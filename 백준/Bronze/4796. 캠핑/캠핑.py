num = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    full_vacation = V // P
    remain = V % P
    useable = full_vacation * L + min(remain, L)

    print(f"Case {num}: {useable}")
    num += 1
