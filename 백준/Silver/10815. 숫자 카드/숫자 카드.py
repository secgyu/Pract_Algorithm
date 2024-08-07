import sys
input = sys.stdin.readline

N = int(input())

card = set(map(int, input().split()))
M = int(input())

card_query = list(map(int, input().split()))

result = []

for c in card_query:
    if c in card:
        result.append('1')
    else:
        result.append('0')

print(*result) 