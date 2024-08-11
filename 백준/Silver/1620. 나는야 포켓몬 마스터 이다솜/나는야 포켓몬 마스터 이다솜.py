import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n+1):
    name = input().rstrip()
    dict[i] = name
    dict[name] = i

for i in range(m):
    question = input().rstrip()
    if question.isdigit():
        print(dict[int(question)])
    else:
        print(dict[question])