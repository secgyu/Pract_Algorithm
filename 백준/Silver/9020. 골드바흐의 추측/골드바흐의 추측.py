import math
import sys
input = sys.stdin.readline


def prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


for i in range(int(input())):
    num = int(input())
    left = num // 2
    right = num - left

    arr = [0, 0]

    while left >= 2:
        if prime(left) and prime(right):
            print(left, right)
            break
        left -= 1
        right += 1
