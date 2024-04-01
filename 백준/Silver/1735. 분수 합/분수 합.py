a, b = list(map(int, input().split(' ')))
c, d = list(map(int, input().split(' ')))

numerator = a * d + b * c
denominator = b * d


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


gcd = gcd(numerator, denominator)

numerator = numerator // gcd
denominator = denominator // gcd

print(numerator, denominator)
