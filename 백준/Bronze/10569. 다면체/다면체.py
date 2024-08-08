T = int(input())

results = []
for _ in range(T):
    V, E = map(int, input().split())
    F = 2 + E - V    
    results.append(F)

for result in results:
    print(result)
