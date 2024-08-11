import math

n = int(input())
radii = list(map(int, input().split()))

R1 = radii[0]

for i in range(1, n):
    Ri = radii[i]
    gcd_value = math.gcd(R1, Ri)

    numerator = R1 // gcd_value
    denominator = Ri // gcd_value

    print(f"{numerator}/{denominator}")