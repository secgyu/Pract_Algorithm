from itertools import combinations

dwarf = [int(input()) for _ in range(9)]

combinations_of_dwarf = combinations(dwarf, 7)

for combo in combinations_of_dwarf:
    if sum(combo) == 100:
        result = sorted(combo)
        for height in result:
            print(height)
        break