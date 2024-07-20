import sys
input = sys.stdin.readline
n = int(input())

result = 0

human = 1

while human * human <= n:
    human = human + 1
    result = result + 1
print(result)
