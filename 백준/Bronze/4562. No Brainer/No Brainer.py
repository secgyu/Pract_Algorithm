def evaluate_brain_consumption(n):
    results = []
    for _ in range(n):
        X, Y = map(int, input().split())
        if X >= Y:
            results.append("MMM BRAINS")
        else:
            results.append("NO BRAINS")
    return results

n = int(input())

results = evaluate_brain_consumption(n)
for result in results:
    print(result)
