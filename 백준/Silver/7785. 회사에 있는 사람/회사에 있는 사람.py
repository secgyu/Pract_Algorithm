import sys
input = sys.stdin.readline

N = int(input())
company = set()

for _ in range(N):
    name, state = input().split()

    if state == 'enter':
        company.add(name)
    else:
        company.remove(name)

result = list(sorted(company, reverse=True))

for i in range(len(result)):
    print(result[i])