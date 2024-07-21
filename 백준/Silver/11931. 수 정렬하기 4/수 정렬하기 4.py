import sys
input = sys.stdin.readline

count = int(input())
arr = []

for _ in range(count):
    arr.append(int(input()))

arr.sort(reverse=True)

for num in arr:
    print(num)
