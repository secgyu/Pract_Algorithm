import sys
input = sys.stdin.readline

count = int(input())
arr = [0] * 10001

for _ in range(count):
    arr[int(input())] += 1

for i in range(len(arr)):
    for _ in range(arr[i]):
        print(i)
