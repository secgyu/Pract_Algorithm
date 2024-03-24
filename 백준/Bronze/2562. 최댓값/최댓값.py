findmax = []
for i in range(9):
    i = int(input())
    findmax.append(i)

print(max(findmax))
print(findmax.index(max(findmax))+1)
