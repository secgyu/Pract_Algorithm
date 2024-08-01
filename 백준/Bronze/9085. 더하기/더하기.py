import sys

input = sys.stdin.read
data = input().split()

T = int(data[0])
index = 1

for _ in range(T):
    N = int(data[index])
    numbers = map(int, data[index + 1:index + 1 + N])
    print(sum(numbers))
    index += N + 1
