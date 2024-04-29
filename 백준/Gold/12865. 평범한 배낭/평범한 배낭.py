# input() # '4 7' -> [4, 7]
# input().split() # ['4', '7']
# list(map(int, input().split())) # [4, 7]

memo = {}
k, weight = map(int, input().split())
w = [0]
p = [0]

for i in range(k):
    ww, pp = map(int, input().split())
    w.append(ww)
    p.append(pp)


def knapsack(k, weight):
    if k == 0 or weight == 0:
        return 0
    if (k, weight) in memo:
        return memo[k, weight]

    if weight < w[k]:
        memo[k, weight] = knapsack(k-1, weight)
    else:
        memo[k, weight] = max(knapsack(k-1, weight),
                              knapsack(k-1, weight-w[k])+p[k])

    return memo[k, weight]


print(knapsack(k, weight))
