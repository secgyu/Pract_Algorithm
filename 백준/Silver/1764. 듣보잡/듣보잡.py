import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = set()
s2 = set()
for i in range(N):
    s.add(input().rstrip())

for i in range(M):
    s2.add(input().rstrip())

result = sorted(s.intersection(s2))
print(len(result))
for i in result:
    print(i)