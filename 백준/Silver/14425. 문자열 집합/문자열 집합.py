import sys
input = sys.stdin.readline

count = 0
s = set()
n, m = map(int, input().split())

for _ in range(n):
    string = input()
    s.add(string)

for _ in range(m):
    string2 = input()
    if string2 in s:
        count +=1

print(count)
