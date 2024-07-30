def num(n):
    if n == 0:
        return
    else:
        num(n // 2)
        print(n % 2, end='')


n = int(input())
num(n)
