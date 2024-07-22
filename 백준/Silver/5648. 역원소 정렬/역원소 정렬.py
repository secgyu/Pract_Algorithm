import sys
input = sys.stdin.readlines()

num = []
for i in input:
    for j in i.split():
        num.append(int(j[::-1]))
num = num[1:]
num.sort()
print("\n".join(map(str,num)))