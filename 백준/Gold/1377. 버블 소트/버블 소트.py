import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append((int(input()), i))

max_num = 0
sorted_arr = sorted(arr)

for i in range(n):
    if max_num < sorted_arr[i][1] - i:
        max_num = sorted_arr[i][1] - i
print(max_num+1)
