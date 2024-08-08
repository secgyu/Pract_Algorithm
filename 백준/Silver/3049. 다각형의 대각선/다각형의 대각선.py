import math

n = int(input())
if n < 4:
    print(0)
else :
    intersection = math.comb(n, 4)
    print(intersection)