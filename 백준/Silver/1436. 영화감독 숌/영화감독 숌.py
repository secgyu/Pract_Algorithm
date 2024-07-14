n = int(input())
count = 0
a = 666

while True:
    if '666' in str(a):
        count += 1
    if count == n:
        break
    a += 1
print(a)
