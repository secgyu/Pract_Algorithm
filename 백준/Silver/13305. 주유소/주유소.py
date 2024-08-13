import sys
input = sys.stdin.readline

n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_cost = 0
min_price = prices[0]

for i in range(n - 1):
    if prices[i] < min_price:
        min_price = prices[i]
    min_cost = min_cost + min_price * distances[i]
print(min_cost)