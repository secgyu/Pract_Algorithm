dish = input()

total_height = 10

for i in range(1, len(dish)):
    if dish[i] == dish[i-1]:
        total_height += 5
    else:
        total_height += 10

print(total_height)
