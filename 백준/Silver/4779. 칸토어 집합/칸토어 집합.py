import sys
input = sys.stdin.read

def slice(N):
    if N == 1:
        return '-'
    else:
        left = slice(N//3)
        center = " " * (N//3)
        return left + center + left

N = input().split()

for i in N:
    i = int(i)
    print(slice(3**i))