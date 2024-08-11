import sys
input = sys.stdin.readline

N, M = map(int, input().split())

s = set(map(int, input().split()))

s2 = set(map(int, input().split()))

result1 = s.difference(s2)
result2 = s2.difference(s)
print(len(result1) + len(result2))