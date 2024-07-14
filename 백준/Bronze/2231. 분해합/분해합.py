n = int(input())

result = 0

for i in range(1, n+1):
    tmp = sum(map(int, str(i))) + i
    if tmp == n:
        print(i)
        break
    if i == n:
        print(0)
