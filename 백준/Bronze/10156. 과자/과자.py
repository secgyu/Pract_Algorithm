k, n, m = map(int, input().split())

money = k*n - m

if money < 0:
    print(0)
else:
    print(money)
